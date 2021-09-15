num = int(input("enter your number: "))
if num > 0:
    print("its a positive number")
    if type(num) == int:
        print("its a positie integer number ")
    else:
        print("float")
else:
    print("its a negetive number")