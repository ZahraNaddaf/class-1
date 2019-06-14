
secret = 7

while True:
    answer = input("guess:",)
    answer = int(answer)
    if answer > secret:
        print("secret is lesser than your number")

    elif answer < secret:
       print("secret is greater than your number")

    elif answer == secret:
        print("True")