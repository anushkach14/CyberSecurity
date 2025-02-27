import itertools
import time

# Brute-force password cracking function
def brute_force(target_password):
    # Define the character set: lowercase, uppercase, and digits
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    # Start with length 1 and increment as needed
    length = 1
    
    while True:

        for attempt in itertools.product(chars, repeat=length):

            guess = ''.join(attempt)
            print(f"Trying: {guess}")

            if guess == target_password:
                return guess
      
        length += 1

if __name__ == "__main__":
    target = "abc123" 
    print("Starting brute-force...")

    start_time = time.time()

    result = brute_force(target)

    print(f"Password cracked: {result}")
    print(f"Time taken: {time.time() - start_time} seconds")