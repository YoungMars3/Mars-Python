number = int(input("Enter a number: "))
counter, total = 1, 0

while counter <= number:
    total = total + counter
    counter = counter + 1

print("Number:", number)
print("Counter:", counter)
print("Total:", total)
print("Result:", float(total) / (counter - 1))
