### Handling Exceptions in Python

In Python, programs can encounter errors, called **exceptions**. To prevent crashes, we use `try` and `except`:

- **`try`**: Python attempts to run the code inside this block. If an error occurs, it stops here and passes control to the `except` block.
- **`except ValueError as e`**: Catches a specific error type (`ValueError`) and gives the actual **error object** a name `e`.
- **`ValueError`**: The **class (blueprint)** of the error.
- **`e`**: The **actual exception object** that Python creates when the error occurs.
- **`print(e)`**: Shows the message stored in the error object.
- **`type(e)`**: Shows which class (blueprint) the error object was made from.

**Difference Between `=` and `as`:**

- **`=` (assignment)**: Gives a name to a class or value. Nothing happens, no error is created.  
  ```python
  e = ValueError  # e now points to the class ValueError itself
  ```
 - as (in except): Gives a name to the error object that Python just created when an exception occurs.

 ```python
 try:
    int("abc")
except ValueError as e:
    print(e) 
```

#### Key Points:

    Using as e allows you to inspect the error object or print its message without crashing the program.

    You can also use type(e) to check which blueprint/class was used to create the error object.

#### Analogy:

    ValueError = blueprint of a house

    Python raises an error → builds the house (error object)

    as e = gives a name to the house so you can look inside

    print(e) = see the contents of the house

    type(e) = see which blueprint was used to build the house

#### Example:

```py
try:
    int("abc")  # This will fail and create a ValueError object
except ValueError as e:
    print(ValueError)  # prints the class itself
    print(e)           # prints the error message
    print(type(e))     # prints <class 'ValueError'>
```
