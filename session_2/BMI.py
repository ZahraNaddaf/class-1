

weight = int(input("enter weight (kg) : "))
height = int(input("enter height (m) : "))

a = 18.5
b = 25
c = 30

BMI = weight/(height**2)

print("BMI =" , BMI)

if BMI < a:
    print("Under-weight")

elif a <= BMI < b:
    print("Normal!")

elif b <= BMI < c:
    print("Over-weight")

elif BMI >= c:
    print("Obesity")
