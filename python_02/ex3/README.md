# Exercise 3: Finally Block - Always Clean Up

This exercise is about validating input data and raising custom ValueError exceptions when values are incorrect, then catching and handling those errors using try / except.

The `finally` block is part of exception handling and **always executes**, whether an error occurs or not.  
It does not clean anything automatically, but it is used to place **cleanup code** (such as closing a system or releasing resources).

- `try` → code that may cause an error  
- `except` → handles the error if it happens  
- `finally` → runs in all cases (with or without error)

The goal of this exercise is to understand that important code (like closing the watering system) must always run, even when an error occurs.

## Understanding `None` in Python

- `None` is a special object that represents **no value** or **nothing here**.  
- It is **different from** `0`, `""` (empty string), or `False`.  
- In this exercise, `plant = None` means there is **no valid plant**, so the program raises an error to prevent watering a nonexistent plant.

## 🌱 Finally Block and Cleanup

- **Cleanup** = safely closing or releasing resources (files, systems, memory) so the program ends safely.  
- **`finally`** = a block that always runs inside a `try`, whether an error occurs or not, ensuring cleanup happens.  
- **`None`** = a special value meaning “no value”; using it where a real value is expected can cause errors.  
- In exercises, `finally` ensures the watering system closes even if a plant is invalid (`None`).  
- Together, `finally` + proper cleanup keeps programs **stable and safe**, even with errors.
