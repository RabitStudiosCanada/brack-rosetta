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
