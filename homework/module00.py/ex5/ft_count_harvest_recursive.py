import time

def ft_count_harvest_recursive(days):
    if days == 0:
        print("Harvest time!")
    else:
        print(f"{days} day(s) until harvest.")
        time.sleep(0.5)
        ft_count_harvest_recursive(days - 1)

    
n = int(input("Days until harvest: "))
ft_count_harvest_recursive(n)