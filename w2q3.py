def gcd(a,b):
    while b != 0:
        a,b=b,a%b
    return a

def coprime(a,b):
    return gcd(a,b) == 1

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

if coprime(x,y):
    print(f"{x} and {y} are relatively prime.")
else:
    print(f"{x} and {y} are not relatively prime.")