import time

def grow(plant):
    plant[1] += 1

def age(plant):
    plant[2] += 1


def ft_garden_growth(packet):
    day = 0 
    while day <= 7:
        print(f"=== Day {day} ===")
        day += 1
        print(f"{packet[0]}: {packet[1]}cm, {packet[2]} days old")
        time.sleep(0.5)
        if day > 0:
            grow(packet)
            age(packet)

x = input("Enter the name of the  plant: ")
y = int(input("Enter the height of the plant in cm: "))
z = int(input("Enter the age of the plant in days: "))
packet = [x, y, z]

ft_garden_growth(packet)