

---

- Create 3 custom exception classes
- raise them in functions
- catch them with try/except
- and demonstrate that a parent error class can catch all child errors.

---

- This exercise teaches how to create custom exception classes
- use inheritance to organize related errors
- and handle them with try/except.
- Custom errors make programs clearer and more specific than Python’s built-in exceptions.
- Inheritance allows catching either specific errors or all garden-related errors using a base class.

---

***In our garden program, `GardenError` is the parent of `PlantError` and `WaterError`:***

```
GardenError
├─ PlantError
└─ WaterErro
```
***It groups all garden-related errors in one place, but there’s an important Python rule: **any error we want to raise must inherit from `Exception`**. Python only knows how to handle classes that come from `BaseException`, so if we tried this:***

```python
class GardenError:
    pass

raise GardenError("Oops")  # ❌ TypeError: exceptions must derive from BaseException

 would fail.
```
By inheriting from Exception, GardenError becomes a proper Python error while still acting as the parent for all our garden-specific errors. This lets us do neat things like:

- Catch only PlantError if we want

- Catch all garden errors at once with GardenError

- Keep our error hierarchy clean and organized

***So even though GardenError is the parent of PlantError and WaterError in our garden world, it’s also a child of Python’s Exception class. This makes it both usable by Python and meaningful in our program.***
