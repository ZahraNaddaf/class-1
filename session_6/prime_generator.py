
def is_prime(number):
    import math

    prime = True
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            prime = False
            break
    return prime




def prime_generator():






