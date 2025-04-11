from math import gcd

def is_additive_group(n):
    # (Z_n, +) is always an abelian group
    return n > 1

def is_ring(n):
    # (Z_n, +, *) always forms a ring for n > 1
    return n > 1

def is_field(n):
    # Z_n is a field iff n is prime
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_structure(n):
    print(f"\nChecking structure for Z_{n}:")
    print("Is Group (additive)?", is_additive_group(n))
    print("Is Ring?", is_ring(n))
    print("Is Field?", is_field(n))

# Example usage:
n = int(input("Enter a number n to analyze Z_n: "))
check_structure(n)
