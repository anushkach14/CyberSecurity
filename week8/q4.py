"""1 - I generate a random integer a as my private key
2 - I generate my public key A by computing aG
3 - You generate a random integer b as your private key
4 - You generate your public key B by computing bG
5 - We exchange public keys
6 - I calculate K as aB
7 - You calculate K as bA"""

from tinyec import registry
import secrets

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

alicePrivKey = secrets.randbelow(curve.field.n)     # Alice's private key
alicePubKey = alicePrivKey * curve.g                # Alice's public key (private key * base point)
print("Alice public key:", compress(alicePubKey))

bobPrivKey = secrets.randbelow(curve.field.n)           # Bob's private key
bobPubKey = bobPrivKey * curve.g                        # Bob's public key (private key * base point)
print("Bob public key:", compress(bobPubKey))

print("Now exchange the public keys (e.g. through Internet)")

aliceSharedKey = alicePrivKey * bobPubKey
print("Alice shared key:", compress(aliceSharedKey))

bobSharedKey = bobPrivKey * alicePubKey
print("Bob shared key:", compress(bobSharedKey))