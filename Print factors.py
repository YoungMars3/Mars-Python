def find_factors_and_compare():
    num = int(input("Enter a number: "))
    factors = [i for i in range(1, num + 1) if num % i == 0]

    sum_of_factors = sum(factors)

    if sum_of_factors > num:
        print(f"The sum of the factors ({sum_of_factors}) is greater than the input number ({num}).")
    elif sum_of_factors < num:
        print(f"The sum of the factors ({sum_of_factors}) is less than the input number ({num}).")
    else:
        print(f"The sum of the factors ({sum_of_factors}) is equal to the input number ({num}).")

find_factors_and_compare()
