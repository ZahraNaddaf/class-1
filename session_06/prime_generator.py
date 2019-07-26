def is_prime(number):
    import math

    prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            prime = False
            break
    return prime


def prime_generator():
    i = 1
    yield i
    while True:
        i += 2
        if is_prime(i):
            yield i


for i in prime_generator():
     print(i)




import time

n=1000


t_i = time.time()
out = list(prime_generator(n))
t_e= time.time()
print("elapsed time  :", t_e - t_i, len(out))