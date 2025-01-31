def narc_numbers(n):
    start = 10**(n-1) 
    end = 10**n    
    narc_nums = []

    for num in range(start, end):
        sum_of_powers = sum(int(digit) ** n for digit in str(num))
        if sum_of_powers == num:
            narc_nums.append(num)

    return narc_nums

n = int(input("Enter value of 'n': "))

result = narc_numbers(n)
print(f"The {n}-digit narcissistic numbers are: {', '.join(map(str, result))}")
