"""Brack parser package."""

from .grammar import validate_text, ParseError

__all__ = ["ParseError", "validate_text"]
