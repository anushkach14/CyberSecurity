def power(G, a, p):
    if a == 1:
        return a
    else:
        return pow(G, a) % p

P = 23
print("The value of P:", P)

G = 9
print("The value of G:", G)

a = 4
print("The private key a for Alice:", a)

x = power(G, a, P)
print("Alice's public key:", x)

b = 3
print("The private key b for Bob:", b)

y = power(G, b, P)
print("Bob's public key:", y)

ka = power(y, a, P)
kb = power(x, b, P)

print("Secret key for Alice is:", ka)
print("Secret key for Bob is:", kb)