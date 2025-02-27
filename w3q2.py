n=int(input("Enter a number: "))
k = 1

while k<n:
    if( pow( 2, k) - 1 == n):
        print (f" {n} is a mersenne prime")
        break
    if( pow( 2, k) >= n):
        print (f" {n} is not a mersenne prime")
        break
    else:
        k+=1
        
