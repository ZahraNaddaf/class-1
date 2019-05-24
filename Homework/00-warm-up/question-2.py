# BMI

a = 18.5
b = 25
c = 30


quest = input("do you want to use standard units? (y/n) : " )

if quest == "y":


    weight = float(input("enter weight (kg) : "))
    height = float(input("enter height (m) : "))


    bmi = weight / (height ** 2)

    print ("BMI =", bmi)



if quest == "n" :


    weight = float(input("enter weight (lb) : "))
    height = float(input("enter height (inch) : "))


    bmi = (weight / (height ** 2))*703

    print("BMI =", bmi)

if bmi < a:
    print("Underweight")

elif a <= bmi < b:
    print("Normal!")

elif b <= bmi < c:
    print("Overweight")

elif bmi >= c:
    print("Obesity")
