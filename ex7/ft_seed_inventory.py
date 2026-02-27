def ft_seed_inventory(veg: str, num: int, unit: str):
    vegname = veg.capitalize()
    if unit = "packets":
        print(f"{vegname} seeds: {num} {unit} available")
    elif unit = "grams":
        print(f"{vegname} seeds: {num} {unit} total")
    elif unit = "area":
        print(f"{vegname} seeds: covers {num} square meters")
    else: 
        print("Unknown unit type")
    