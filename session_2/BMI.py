

weight = 60
height = 1.80

a = 18.5
b = 25
c = 30

BMI = weight/(height**2)

print("BMI =" , BMI)

if BMI < a:
    print("Under-weight")

if a <= BMI < b:
    print("Normal!")

if b <= BMI < c:
    print("Over-weight")

if BMI >= c:
    print("Obesity")
