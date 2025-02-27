import math
def euler(n):
    count=0
    for i in range(1,n):
        if math.gcd(i,n)==1:
            count+=1
    return count

n=int(input("Enter a number: "))
print("eulers totient is: ",euler(n))
