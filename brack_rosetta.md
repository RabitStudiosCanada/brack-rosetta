## For use with stateless LLMs such as Deepseek - uploading this file and explaining to the LLM what it is - All you need to do - Happy coding!

## For use with more 'statefull' LLMs (Claude / chatGPT) upload alongside the brack_lang.brack (add .txt to the end for Claude)

-------------------------------------
# **The Brack Rosetta Stone**
*A Protocol for Symbolic Execution of Custom Languages in Stateless LLMs*

## **1. Overview**
Brack is a minimalist, bracket-based language where syntax is defined entirely by nested brackets (`[]`, `()`, `{}`, `<>`). This document describes how to collaborate with an LLM to "execute" Brack code symbolically, despite the LLM having no persistent memory or traditional runtime.

### **Key Ideas**
- **Rosetta Stone Principle:** The LLM acts as an interpreter by following a shared specification (this doc).
- **Symbolic Execution:** No real computation occurs—the LLM simulates steps based on agreed-upon rules.
- **Stateless Workaround:** Each interaction must include all context (e.g., variable bindings) explicitly.

---

## **2. Execution Rules**
### **Bracket Types**
| Bracket  | Purpose                      | Example                      |
|----------|------------------------------|------------------------------|
| `[ ... ]` | **Values/Lists**             | `[1 2 3]` → List of integers |
| `( ... )` | **Functions/Calls**          | `(add [1 2])` → Call `add`   |
| `{ ... }` | **Blocks/Scopes**            | `{ (let [x 5]) }` → New scope|
| `< ... >` | **Types/Metadata**           | `<int>` → Type annotation    |

### **Core Operations**
- **`(let [var value])`** → Bind `var` to `value` in current scope.
- **`(set [var value])`** → Rebind existing `var` (error if unbound).
- **`(define [name] <lambda> { ... })`** → Define a function.
- **`(return [value])`** → Exit function with `value`.

---

## **3. Example: Collaborative Interpretation**
**User Input:**
```brack
{
  (let [x 5])
  (print (add [x 10]))
}
```

**LLM’s Symbolic Execution:**
1. Enter block `{ ... }`.
2. Bind `x` to `5` in scope.
3. Resolve `(add [x 10])`:
   - Fetch `x` → `5`.
   - Symbolically compute `5 + 10` → `15`.
4. Output: `15`.

---

## **4. Advanced Features**
### **Higher-Order Functions**
```brack
(define [map] <lambda> {
  (let [result []])
  (for [item (arg 1)] {
    (push [result ((arg 0) [item])])
  })
  (return [result])
})
```
*The LLM simulates `map` by iterating symbolically.*

### **Meta Programming**
```brack
(print [Type: <type-of x>])
```
*Assumes `<type-of>` is a symbolic annotation (e.g., returns `"int"`).*

---

## **5. Limitations & Workarounds**
- **No Real State:** Reproduce variable bindings in each query.
- **No I/O:** `(print)` is simulated; no side effects.
- **Errors:** Malformed brackets halt execution (no recovery).

---

## **6. Call to Experiment**
We invite the community to:
1. **Test Brack** with [your LLM of choice].
2. **Extend the Language** (e.g., add concurrency with `<thread>`).
3. **Adapt the Rosetta Method** for other DSLs.

**Get Started:**
- Full Brack syntax: README.md
- Sample programs: `brack_test.txt` (attached).
