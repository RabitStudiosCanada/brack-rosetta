# brack-rosetta
stateless-LLM-Runtime-Hack-Expirimental.jack

# Brack & The Rosetta Stone Protocol  
*A minimalist, bracket-based language symbolically executed by LLMs.*  

<img width="1024" height="1024" alt="Brack_logo" src="https://github.com/user-attachments/assets/94c81a3a-53fa-42d8-9c30-e9359b2a6ff3" />


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
