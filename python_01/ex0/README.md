# 🌱 My Garden - Python Example

A simple Python script to demonstrate the use of the shebang line and the `__main__` pattern in Python.

## 🌟 What You Really Learn

### 1️⃣ Shebang Line: `#! /usr/bin/env python3`

- The shebang (`#!`) tells the operating system which interpreter to use to run the script.  
- Using `/usr/bin/env python3` ensures the **system's default Python 3 interpreter** is used, making your script more portable across different machines.  
- On Linux/macOS, it allows you to run the script directly from the terminal:

```bash
./ft_plant.py
```
#### instead of typing:
```
python3 ft_plant.py
```
-> Without the shebang, the system may not know how to execute the file directly. <br>

### 2️⃣ if __name__ == "__main__":

- Every Python file has a built-in variable called __name__.

- When a script is run directly, __name__ is set to "__main__".

- When a script is imported as a module, __name__ is set to the module’s filename (without .py).

- Using this condition allows you to control execution: code inside this block runs only when the script is executed directly, not when imported.

#### Visual Example

```
my_script.py
 ├─ code outside `if __name__ == "__main__"`  -> runs always
 └─ code inside `if __name__ == "__main__"`  -> runs only when executed directly
```

### ▶️ Execution Behavior Explained

**When the script is executed directly:**

```bash
python3 my_script.py
```
- Python assigns __name__ = "__main__".

- The code inside the if __name__ == "__main__": block is executed.

- This is where the main logic of the program runs.

#### When the script is imported as a module:
```py
import my_script
```
- Python assigns __name__ = "my_script".

- The code inside the if __name__ == "__main__": block is not executed.

- Only definitions (functions, classes, constants) are loaded and made available for reuse in other files.
