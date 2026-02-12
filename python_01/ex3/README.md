# 🌱 Exercise 3 – Plant Factory
#### subject
```
The garden center needs to create many plants quickly using your Plant class with
different starting values. You need to streamline the plant creation process and initialize
them properly.
Requirements:
• Plants need to be created with their initial information (name, starting height,
starting age)
• Each plant should be ready to use immediately after construction
• Create at least 5 different plants with varying characteristics
• Display all created plants in an organized format
• Think about how you can streamline the plant creation process
Consider how you might set up plants with their starting values efficiently. What would
make creating many plants easier?
```
### 📌 What We Learned
- How to **efficiently create multiple Plant objects** from a list of raw data (`plants_data`).  
- The difference between **raw data** (tuples) and **objects**:
  - `plants_data` stores the initial information for each plant.
  - `plants` stores the actual Plant objects created from that data.
- Why keeping raw data separate from objects allows **reusability** and independent manipulation of each object.

### 🖥 Code Explanation

1. **Class Definition**  
   We define a `Plant` class with a method `get_info()` that returns the plant's details as a readable string.

2. **Raw Data**  
   `plants_data` is a list of tuples containing each plant's **name, height, and age**. This acts as our source data.

3. **Creating Plant Objects**  
   Using **list comprehension**, we create a list of `Plant` objects (`plants`) from `plants_data`.  
   This allows creating multiple objects efficiently and independently.

4. **Displaying Plants**  
   We loop through the `plants` list and call `get_info()` on each object to display its information in an organized format.

5. **Total Count**  
   Finally, we print the **total number of plants created**, giving a clear summary of the factory output.

### 📂 Example Output

```
=== Plant Factory Output ===
Created: Rose (25cm, 30 days)
Created: Oak (200cm, 365 days)
Created: Cactus (5cm, 90 days)
Created: Sunflower (80cm, 45 days)
Created: Fern (15cm, 120 days)

Total plants created:
```
