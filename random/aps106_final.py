# find the largest 4 digit prime number

""" prime number = n where only n%n and n%1 ==0 starting from 2

first a function to find the first 10 primes first """

def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number, 'False' otherwise"""
    import math
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for i in range(3, max_divisor + 1, 2):
        if n%i == 0:
            return False
    return True

def prime_checks(count):
    found = 0
    check = 1

    while found <= count:
        if is_prime_v1(check):
            found += 1
            print(check)
        check += 1

def highest_prime():
    n = 9999
    for i in range(9999, 1, -1):
        if is_prime_v1(i):
            print(i)
            return


prime_checks(1300)
