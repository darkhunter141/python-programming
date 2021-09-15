name = input("what is your Username: ")
password = input("what is your password: ")
input1 = None
input2 = None
while input1 != name:
    input1 = input("please enter your current username: ")
while input2 != password:
    input2 = input("please enter your current password: ")
print("welcome back to your system")