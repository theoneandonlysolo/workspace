
class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1

    def info(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_count):
        super().__init__(name, height)
        self.flower_count = flower_count

    def info(self):
        return f"{self.name}: {self.height}cm, flowers: {self.flower_count}"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_count, prize_points):
        super().__init__(name, height, flower_count)
        self.prize_points = prize_points

    def info(self):
        return f"{self.name}: {self.height}cm, flowers: {self.flower_count}, prize points: {self.prize_points}"


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def grow_all(self):
        for plant in self.plants:
            plant.grow()


class GardenManager:
    total_gardens = 0

    class GardenStats:
        @staticmethod
        def count_plants(garden):
            return len(garden.plants)

        @staticmethod
        def total_growth(garden):
            return sum(plant.height for plant in garden.plants)

        @staticmethod
        def count_types(garden):
            regular = 0
            flowering = 0
            prize = 0

            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                elif isinstance(plant, Plant):
                    regular += 1

            return regular, flowering, prize

    def __init__(self):
        self.gardens = []
        GardenManager.total_gardens += 1

    def add_garden(self, garden):
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        return cls()

    @staticmethod
    def validate_height(height):
        return height >= 0

    @staticmethod
    def calculate_score(garden):
        score = 0
        for plant in garden.plants:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        return score

