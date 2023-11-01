def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num_str = input("Enter the number you want:")
num = int(num_str)

print_factors(num)



































