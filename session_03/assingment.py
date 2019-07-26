n = 7
pattern = "*"

for i in range(1, n + 1):
    print(pattern * i)

print("\n")

for i in range(0, n + 1):
    print(" " * (n - i), pattern * (2 * i + 1))

print("\n")

for i in range(0, n + 1):

    if i == 0:
        print(" " * (n), pattern, sep='')
    if 0 < i < n:
        print(" " * (n - i), pattern, " " * (2 * i - 2), pattern, sep='')

    if i == n:
        print(" " * (n - i), pattern * (2 * i + 2), sep='')
