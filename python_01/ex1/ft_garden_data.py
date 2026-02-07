class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus",15, 120)

print("=== Garden Plant Registry ===")
print(rose.get_info())
print(sunflower.get_info())
print(cactus.get_info())
