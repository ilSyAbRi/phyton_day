class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = True


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, prize_points):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

class GardenManager:
    all_gardens = []

    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        GardenManager.all_gardens.append(self)

    def add_plant(self,plant):
        self.plants.append(plant)

    def grow_all_plants(self):
        for plant in self.plants:
            plant.height += 1
    class GardenStats:
        def __init___(self, garden):
            self.garden = garden
        def total_growth(self):
            return sum

rose = FloweringPlant("Rose", 25, "Red")
sunflower = PrizeFlower("Sunflower", 50, "Yellow", 10)

alice = GardenManager("Alice")
bob = GardenManager("Bob")

alice.add_plant(rose)
alice.add_plant(sunflower)
bob.add_plant(FloweringPlant("Tulip", 20, "Pink"))

print("Alice's plants:", [p.name for p in alice.plants])
print("Bob's plants:", [p.name for p in bob.plants])
print("Total gardens:", len(GardenManager.all_gardens))
