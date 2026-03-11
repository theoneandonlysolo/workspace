def ft_garden_data(packet1, packet2, packet3):
    print("=== Garden Plant Registry ===")
    print(f"{packet1[0]}: {packet1[1]}cm, {packet1[2]} days old")
    print(f"{packet2[0]}: {packet2[1]}cm, {packet2[2]} days old")
    print(f"{packet3[0]}: {packet3[1]}cm, {packet3[2]} days old")

x = input("Enter the name of the first plant: ")
y = int(input("Enter the height of the first plant in cm: "))
z = int(input("Enter the age of the first plant in days: "))
packet1 = (x, y, z)

xx = input("Enter the name of the second plant: ")
yy = int(input("Enter the height of the second plant in cm: "))
zz = int(input("Enter the age of the second plant in days: "))
packet2 = (xx, yy, zz)     

xn = input("Enter the name of the third plant: ")
yn = int(input("Enter the height of the third plant in cm: "))
zn = int(input("Enter the age of the third plant in days: "))
packet3 = (xn, yn, zn)

ft_garden_data(packet1, packet2, packet3)