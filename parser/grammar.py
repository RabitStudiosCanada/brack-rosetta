"""Validation utilities for the Brack grammar.

This module implements a small recursive-descent parser that checks whether a
piece of text follows the structural rules laid out in ``docs/GRAMMAR.md``.
It is intended for lightweight validation (e.g. before sharing Brack snippets
with an LLM) rather than for execution.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


class ParseError(Exception):
    """Raised when the input violates the Brack grammar."""

    def __init__(self, message: str, line: int, column: int) -> None:
        super().__init__(f"Line {line}, column {column}: {message}")
        self.message = message
        self.line = line
        self.column = column


@dataclass
class _Position:
    index: int = 0
    line: int = 1
    column: int = 1


class _BrackParser:
    """Simple recursive-descent parser for Brack values."""

    def __init__(self, text: str) -> None:
        self._text = text
        self._pos = _Position()

    # ------------------------------------------------------------------
    # Public entry point
    # ------------------------------------------------------------------
    def parse(self) -> None:
        """Parse an entire document.

        Raises ``ParseError`` if the text is not well-formed.
        """

        self._consume_spacing()
        while not self._eof:
            self._parse_value()
            self._consume_spacing()

    # ------------------------------------------------------------------
    # Core parsing primitives
    # ------------------------------------------------------------------
    @property
    def _current(self) -> Optional[str]:
        if self._pos.index >= len(self._text):
            return None
        return self._text[self._pos.index]

    def _peek(self, offset: int = 0) -> Optional[str]:
        index = self._pos.index + offset
        if index >= len(self._text):
            return None
        return self._text[index]

    @property
    def _eof(self) -> bool:
        return self._pos.index >= len(self._text)

    def _advance(self, count: int = 1) -> None:
        for _ in range(count):
            if self._pos.index >= len(self._text):
                return
            char = self._text[self._pos.index]
            self._pos.index += 1
            if char == "\n":
                self._pos.line += 1
                self._pos.column = 1
            else:
                self._pos.column += 1

    def _expect(self, char: str) -> None:
        if self._current != char:
            if self._current is None:
                raise self._error(f"Expected '{char}' before end of input")
            raise self._error(f"Expected '{char}' but found '{self._current}'")
        self._advance()

    def _error(self, message: str) -> ParseError:
        return ParseError(message, self._pos.line, self._pos.column)

    # ------------------------------------------------------------------
    # Spacing & comments
    # ------------------------------------------------------------------
    def _consume_spacing(self) -> None:
        while not self._eof:
            consumed_whitespace = False
            while not self._eof and self._current is not None and self._current.isspace():
                consumed_whitespace = True
                self._advance()
            if self._current == "/" and self._peek(1) == "/":
                consumed_whitespace = True
                self._advance(2)
                while not self._eof and self._current not in {"\n", "\r"}:
                    self._advance()
                # Consume the newline that terminated the comment, if any.
                if self._current in {"\n", "\r"}:
                    self._advance()
                continue
            if not consumed_whitespace:
                break

    # ------------------------------------------------------------------
    # Value parsing
    # ------------------------------------------------------------------
    def _parse_value(self) -> None:
        if self._current is None:
            raise self._error("Unexpected end of input while reading a value")

        char = self._current
        if char == "[":
            self._parse_list()
        elif char == "(":
            self._parse_call()
        elif char == "{":
            self._parse_block()
        elif char == "<":
            self._parse_meta()
        elif char in "])}>":
            raise self._error(f"Unexpected closing bracket '{char}'")
        else:
            self._parse_atom()

    def _parse_list(self) -> None:
        self._expect("[")
        self._consume_spacing()
        while self._current is not None and self._current != "]":
            self._parse_value()
            self._consume_spacing()
        self._expect("]")

    def _parse_call(self) -> None:
        self._expect("(")
        self._consume_spacing()
        if self._current == ")":
            raise self._error("Function call must contain at least one value")
        self._parse_value()  # operator
        self._consume_spacing()
        while self._current is not None and self._current != ")":
            self._parse_value()
            self._consume_spacing()
        self._expect(")")

    def _parse_block(self) -> None:
        self._expect("{")
        self._consume_spacing()
        while self._current is not None and self._current != "}":
            self._parse_value()
            self._consume_spacing()
        self._expect("}")

    def _parse_meta(self) -> None:
        self._expect("<")
        self._consume_spacing()
        while self._current is not None and self._current != ">":
            self._parse_value()
            self._consume_spacing()
        self._expect(">")

    def _parse_atom(self) -> None:
        start_index = self._pos.index
        while self._current is not None and not self._current.isspace() and self._current not in "[](){}<>":
            # Stop before comment markers if they start immediately after the atom.
            if self._current == "/" and self._peek(1) == "/":
                break
            self._advance()
        if start_index == self._pos.index:
            raise self._error("Expected an atom")

    # ------------------------------------------------------------------
    # Helper API
    # ------------------------------------------------------------------
    def remaining_text(self) -> str:
        return self._text[self._pos.index :]


# ----------------------------------------------------------------------
# Public helpers
# ----------------------------------------------------------------------
def validate_text(text: str) -> bool:
    """Return ``True`` if *text* is valid Brack, otherwise raise ``ParseError``."""

    parser = _BrackParser(text)
    parser.parse()
    return True


def validate_file(path: str) -> bool:
    """Validate the contents of *path*.

    Returns ``True`` when parsing succeeds. ``ParseError`` is raised on failure.
    """

    with open(path, "r", encoding="utf-8") as handle:
        text = handle.read()
    return validate_text(text)


def _main(argv: Optional[list[str]] = None) -> int:
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Validate Brack files against the grammar.")
    parser.add_argument("paths", nargs="*", help="Files to validate. Reads from stdin when omitted.")
    args = parser.parse_args(argv)

    if not args.paths:
        text = sys.stdin.read()
        try:
            validate_text(text)
        except ParseError as error:
            print(error, file=sys.stderr)
            return 1
        return 0

    exit_code = 0
    for path in args.paths:
        try:
            validate_file(path)
        except ParseError as error:
            print(f"{path}: {error}", file=sys.stderr)
            exit_code = 1
        else:
            print(f"{path}: OK")
    return exit_code


if __name__ == "__main__":  # pragma: no cover - CLI helper
    raise SystemExit(_main())
