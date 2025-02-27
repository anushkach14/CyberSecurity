import random
import string

def gen(length=8):
    char=string.ascii_letters + string.digits + string.punctuation
    pswd = "".join(random.choice(char) for i in range(length))
    return pswd

pswd=gen()
print("Password: ",pswd)