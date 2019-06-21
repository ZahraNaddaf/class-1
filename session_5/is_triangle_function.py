def is_triangle(a, b, c):
    out = True
    if a < b + c and b < a + c and c < a + b:
        return out

    else:
        out = False
        return out


x = is_triangle(3, 4, 5)
print(x)
