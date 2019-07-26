num = 1010
i = 2

is_prime = True

while i < num :
    b = num % i
    print(i)
    if b == 0:
        is_prime = False
    i += 1

print(is_prime)
