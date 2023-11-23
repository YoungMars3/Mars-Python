a = int(input("Give a number: "))  # Convert input to an integer
b, c = 1, 0
while b <= a:
    c = c+b
    b = b+1
print(a, b, c)
print("Result: ", float(c)/(b-1))
