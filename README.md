# brack-rosetta v0.1-alpha
stateless-LLM-Runtime-Hack-Experimental.jack

“Language models possess the potential to generate not just incorrect information but also self-contradictory or paradoxical statements... these are an inherent and unavoidable feature of large language models.”

— LLMs Will Always Hallucinate, arXiv:2409.05746 - { https://arxiv.org/html/2409.05746v1 }

   ———— The Brack approach = Lets use this 🧑🏽‍💻⚗️ <-- Rabit Studios - ⛯Lighthouse⛯ Research Group

# Brack & The Rosetta Stone Protocol  
*A minimalist, bracket-based language symbolically executed by LLMs.*  

<img width="1024" height="1024" alt="Brack_logo" src="https://github.com/user-attachments/assets/94c81a3a-53fa-42d8-9c30-e9359b2a6ff3" />

⛯Usage⛯
- Explain to chosen LLM (GPT / Claude / DeepSeek / Gemini / Etc) - What this is and what you would like them to do with it (Polite).
- Upload brack_rosetta.md / brack_lang.brack (if on GPT / Claude) - (if on DeepSeek / Gemini) -> Upload Just brack_rosetta.md by itself.
   - (optional) Upload test program and ask LLM to 'run' it symbolically - to test if LLM instance has understood its task.
- Happy Coding!

## **What is Brack?**  
Brack is a purely bracket-delimited language (`[]`, `()`, `{}`, `<>`) designed to explore **collaborative symbolic execution** with stateless LLMs.  

## **Key Features**  
- **100% Brackets**: No bare words, no ambiguity.  
- **LLM-Friendly**: Designed for Rosetta Stone-style interpretation.  
- **Extensible**: Add your own bracket semantics.  

## **Quick Start**  
1. **Run Symbolically**: Paste Brack code into an LLM (like DeepSeek Chat) with the [Rosetta Stone rules](docs/BRACK_SPEC.md).  
   ```brack
   { (print (add [1 2])) }

________________________________________________________________________________________________________________________________________________________

# **Brack Syntax Overview**

**Language Philosophy:**

* **All code is bracketed.**
* **No bare words, no quotes.**
* **Everything is a symbolic operation or structure.**
* **Whitespace is ignored outside brackets.**

---

### **Bracket Meanings**

| Bracket  | Symbol | Primary Use                        |
| -------- | ------ | ---------------------------------- |
| \[ ... ] | Square | Values & Lists                     |
| ( ... )  | Round  | Function Calls / Operations        |
| { ... }  | Curly  | Blocks / Scopes / Objects          |
| < ... >  | Angle  | Types / Modifiers / Meta / Symbols |

---

## **SYNTAX EXAMPLES**

### 1. **Values & Lists**

* `[1 2 3]` — a list of numbers
* `[true false true]` — booleans

### 2. **Function Calls**

* `(add [1 2])` — call `add` on list `[1 2]`
* `(print [Hello World])` — print a list

### 3. **Blocks/Objects**

* `{ (let [x 5]) (let [y 10]) (add [x y]) }` — a block with two variables and an operation

### 4. **Types/Meta**

* `<int>` — type int
* `<list<int>>` — list of ints
* `<lambda>` — lambda/function

---

### **Putting It All Together**

```brack
{                   // Block (scope)
  (let [x 5])       // Define x
  (let [y 10])      // Define y
  (print (add [x y]))
}
```

---

### **Defining Functions**

```brack
(define [add2]
  <lambda>
  { (let [x (arg 0)]) (let [y (arg 1)]) (add [x y]) }
)
```

* `(define [add2] ...)` — defines a function
* `<lambda>` — denotes it's a function
* `(arg 0)` — gets argument 0

---

### **If/Else**

```brack
(if (gt [x 5])
    { (print [Greater]) }
    { (print [LesserOrEqual]) }
)
```

---

### **Looping**

```brack
(for [i [1 2 3 4]]
    { (print [i]) }
)
```

---

### **Symbolic / Meta Programming**

* `<symbol:add>` — symbol named "add"
* `<meta:[compile-time]>` — meta info

---

## **Symbolic Power Moves**

You can compose code by treating brackets as building blocks:

* `[ (add [x y]) (sub [y x]) ]` — a list of operations
* `{ ... }` blocks can be passed around as first-class citizens
* `<...>` lets you build your own type system / meta logic

---

## **Sample Program (Hello, World!)**

```brack
{ (define [main] <lambda> { (print [Hello, World!]) }) (main) }
```

---

## **Summary Table**

| Concept      | Example Brack Syntax            |
| ------------ | ------------------------------- |
| List         | `[1 2 3]`                       |
| Call         | `(add [1 2])`                   |
| Block/Scope  | `{ ... }`                       |
| Type/Meta    | `<int>` `<lambda>`              |
| Function Def | `(define [f] <lambda> { ... })` |
| If           | `(if ... { ... } { ... })`      |
| For          | `(for [i xs] { ... })`          |

---

## **Final Thoughts**

* **No strings:** everything is a bracketed symbol or value list (`[Hello World]` is a list of symbols, not a string)
* **No operators:** use function calls like `(add [a b])`, `(gt [a b])`
* **Compositional:** all structures are recursively bracketed

________________________________________________________________________________________________________________________________________________________

    Note: Brack is a thought experiment—it has no runtime, only symbolic LLM execution.

text


---

#### **B. `docs/BRACK_SPEC.md`** *(Full Language Spec)*  
```markdown
# Brack Language Specification  
### **1. Bracket Types**  
| Bracket  | Purpose                | Example              |  
|----------|------------------------|----------------------|  
| `[ ... ]` | Values/Lists          | `[1 2 3]`            |  
| `( ... )` | Function Calls        | `(add [1 2])` → `3`  |  
| `{ ... }` | Blocks/Scopes         | `{ (let [x 5]) }`    |  
| `< ... >` | Types/Metadata        | `<int>`, `<lambda>`  |  

### **2. Core Functions**  
- `(let [var value])` → Bind `var` to `value`.  
- `(set [var value])` → Rebind `var` (error if unbound).  
- `(define [name] <lambda> { ... })` → Define a function.  

### **3. Symbolic Execution Rules**  
- The LLM simulates evaluation step-by-step.  
- No persistent state—redeclare variables in each query.  
- **Example**:  
  ```brack
  { (let [x 5]) (print (add [x 10])) }  // → 15
```
text


---
```markdown
#### **C. `examples/factorial.brack`** *(Demo File)*  
```brack
{
  (define [factorial] <lambda> 
    { (if (eq [n 0]) 
        { [1] } 
        { (mul [n (factorial (sub [n 1]))]) } 
    })
  (print (factorial [5]))  // → 120
}
```

(CC BY 4.0) Rabit Studios - ⛯Lighthouse⛯ Research Group  <----- We would love to know what you make with this - Please reach out! [Rabit's Warren Discord Channel: Join<https://discord.gg/8BuTBHtyac>]

WANT MORE AI TOOLS?
GO check out drtacrine's AxisBridge-USPP-Kit v0.1 – Symbolic Agent Protocol !
- An experimental Ethical AI Agent Framework - (one that can say no to you)
- Axis AI Agents Are able to communicate with our Lantern-kin AI Via USPPv4 w/ full Support !

CREATOR SHOWCASE: https://github.com/drtacine/AxisBridge-USPP-Kit/releases

