
def ft_garden_intro(name, height,age):
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    if age > 1:
        print(f"Age: {age} days")
    if age == 1:
        print(f"Age: {age} day")
    print("\n=== End of Program ===")

plant_name = input("Enter the plant name: ")
plant_height = int(input("Enter the plant height in cm: "))
plant_age = int(input("Enter the plant age in days: "))

if plant_age < 0:
    print("Age cannot be negative. Please enter a valid age.")

if plant_height < 0:
    print("Height cannot be negative. Please enter a valid height.")

ft_garden_intro(plant_name, plant_height, plant_age)