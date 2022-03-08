i = 0
while i <= 2:
    print("Please enter an integer")
    a = input()
    a = int(a)
    if a <= 0:
        print("Please type in an integer")
        i = i + 1
    else:
        if a % 2 == 0:
            print("This number is the multiple of 2")
        else:
            print("This number is not the multiple of 2")
        if a % 3 == 0:
            print("This number is the multiple of 3")
        else:
            print("This number is not the multiple of 3")
        if a % 4 == 0:
            print("This number is the multiple of 4")
        else:
            print("This number is not the multiple of 4")
        break
else:
    print("You enter wrong number more than 3 times, please try it later")