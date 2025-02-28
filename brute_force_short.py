import itertools
import time

def brute_force(target_pswd):
    chars='0123456789abcdefghijklmnopqrstuvwxyz'
    target_pswd_lower = target_pswd.casefold()
    for i in itertools.product(chars, repeat=len(target_pswd)):
        if ''.join(i)==target_pswd_lower:
            return f"Password cracked: {target_pswd}"

pswd=input("Enter your pswd: ")
start_time=time.time()

print(brute_force(pswd))

print(f"Time taken: {time.time()-start_time} seconds")