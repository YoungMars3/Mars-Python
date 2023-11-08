integer = int(input("Give a number: "))  # Convert input to an integer
pinteger, total = 1, 0
while pinteger <= integer:
    total = total+pinteger
    pinteger = pinteger+1
print(integer, pinteger, total)
print("Result: ",float(total)/(pinteger-1))