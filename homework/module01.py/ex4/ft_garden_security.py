class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = 0
        self.__age = 0

        self.set_height(height)
        self.set_age(age)

    def set_height(self, value: int):
        if value < 0:
            print("Error: Height cannot be negative.")
            return
        self.__height = value

    def set_age(self, value: int):
        if value < 0:
            print("Error: Age cannot be negative.")
            return
        self.__age = value

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name


def ft_garden_security(packet):
    plant = SecurePlant(packet[0], packet[1], packet[2])
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.get_name()} [OK]")
    print(f"Height updated: {plant.get_height()}cm [OK]")
    print(f"Age updated: {plant.get_age()} days [OK]")
    print("Security Status: All clear!")
