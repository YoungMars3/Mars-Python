a = int(input("Give a number: "))  # Specifying a's type as an integer
b, c = 1, 0                        # b and c are integers initially
while b <= a:
    c = c+b
    b = b+1
print(a, b, c)
print("Result: ", float(c)/(b-1)) # Converting c to float before calculation
