def square_numbers_gen():
    i = 1
    while True:
        b = i ** 2

        yield b
        i += 1


gen = square_numbers_gen()
for i in gen:
    print(i)
