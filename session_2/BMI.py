

weight = float(input("enter weight (kg) : "))
height = float(input("enter height (m) : "))

a = 18.5
b = 25
c = 30

bmi = weight / (height ** 2)

print("BMI =", bmi)

if bmi < a:
    print("Under-weight")

elif a <= bmi < b:
    print("Normal!")

elif b <= bmi < c:
    print("Over-weight")

elif bmi >= c :
    print("Obesity")
