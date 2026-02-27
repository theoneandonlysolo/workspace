import time

def ft_count_harvest_recursive():
    daysuntil = int(input("Days until harvest: "))
    i = 1
    while i <= daysuntil:
        time.sleep(0.5)
        print(f"Day {i}")
        i += 1
    print("Harvest time!")
