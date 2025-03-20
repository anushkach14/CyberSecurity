import random
P=23
G=5

a=random.randint(1,P-1)
A=(G**a)%P

b=random.randint(1,P-1)
B=(G**b)%P

shared_secret_alice=(B**a)%P
shared_secret_bob=(A**b)%P

print(f"Alice publ;ic key : {A}")
print(f"Bob public key : {B}")
print(f"Shared secret alice : {shared_secret_alice}")
print(f"shared secret bob: {shared_secret_bob}")
