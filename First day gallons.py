inches_str = input("How many inches of rain has fallen:")
inches_int = int(inches_str)
volume = (inches_int/12)*43560
gallons = volume * 7.48051945
print(inches_str,"in. rain on 1 acre is", gallons, "gallons")