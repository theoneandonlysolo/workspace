def ft_plant_factory(plant1, plant2, plant3, plant4, plant5):
    print("=== Plant factory output ===")
    print(f"Created: {plant1[0]} ({plant1[1]}cm, {plant1[2]} days)")
    print(f"Created: {plant2[0]} ({plant2[1]}cm, {plant2[2]} days)")
    print(f"Created: {plant3[0]} ({plant3[1]}cm, {plant3[2]} days)")
    print(f"Created: {plant4[0]} ({plant4[1]}cm, {plant4[2]} days)")
    print(f"Created: {plant5[0]} ({plant5[1]}cm, {plant5[2]} days)")
    print("\nTotal plants created: 5")

x = input("Enter the name of the first plant: ")
y = int(input("Enter the height of the first plant in cm: "))
z = int(input("Enter the age of the first plant in days: "))
plant1 = [x, y, z]

xx = input("Enter the name of the second plant: ")
yy = int(input("Enter the height of the second plant in cm: "))
zz = int(input("Enter the age of the second plant in days: "))
plant2 = [xx, yy, zz]

xn = input("Enter the name of the third plant: ")
yn = int(input("Enter the height of the third plant in cm: "))
zn = int(input("Enter the age of the third plant in days: "))
plant3 = [xn, yn, zn]

xm = input("Enter the name of the fourth plant: ")
ym = int(input("Enter the height of the fourth plant in cm: "))
zm = int(input("Enter the age of the fourth plant in days: "))
plant4 = [xm, ym, zm]

xp = input("Enter the name of the fifth plant: ")
yp = int(input("Enter the height of the fifth plant in cm: "))
zp = int(input("Enter the age of the fifth plant in days: "))
plant5 = [xp, yp, zp]

ft_plant_factory(plant1, plant2, plant3, plant4, plant5)