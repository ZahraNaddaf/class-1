def fibonacci(n):
    if n in (1, 2):
        return 1

    res = fibonacci(n - 1) + fibonacci(n - 2)
    return res


for i in range (1, 20):
    print(fibonacci(i))