import random

def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)
    print(f"GCD of {a} and {b} is {euclid(a, b)}")