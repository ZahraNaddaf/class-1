
def is_prime(number):
    import math

    prime = True
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            prime = False
            break
    return(prime)


result = is_prime(11098751357)
print(result)





