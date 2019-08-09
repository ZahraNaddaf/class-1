import math


def is_prime(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def is_super_prime(n):
    if n < 10:
        return is_prime(n)

    if is_super_prime(n // 10):
        return is_prime(n)


def list_of_super_primes(lower, upper):
    return filter(is_super_prime, range(lower, upper))


print(list(list_of_super_primes(1000, 100000)))
