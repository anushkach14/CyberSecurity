def mod_inverse(a, p):
    return pow(a, p - 2, p)

a = int(input("Enter a (number to find inverse of): "))
p = int(input("Enter p (a prime number as modulus): "))
inverse = mod_inverse(a, p)
print(inverse)  
