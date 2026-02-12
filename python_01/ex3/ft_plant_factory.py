class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


plants_data = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]
plants = [Plant(name, height, age) for name, height, age in plants_data]
print("=== Plant Factory Output ===")
for p in plants:
    print(p.get_info())
print("\nTotal plants created: 5")
