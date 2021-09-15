user={}
status=""
import re

def displayMenu():
    status = input("Are you registered user? y/n ")
    if status == "y":
        oldUser() 
    elif status == "n":
        newUser()
            
def newUser():
    
    createLogin = input("Create login email-id: ")
    if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",createLogin,re.IGNORECASE):
        print("valid")

    else:
        print("Email is invalid")
    

    if createLogin in user:
        print("\nLogin email already exists!\n")
    else:
        
        while True:
        
            createPwd = input("create Password: ")
            if len(createPwd) < 8:
                print("Make sure your password is at lest 8 letters")
            elif re.search('[0-9]', createPwd) is None:
                print("Make sure your password has a number in it")
            elif re.search('[A-Z]', createPwd) is None: 
                print("Make sure your password has a capital letter in it")
            elif re.search('[a-z]', createPwd) is None: 
                print("Make sure your password has a small letter in it")
            else:
                print("Your password seems fine")
                user[createLogin] = createPwd
                print("\nUser create\n")
                break

def oldUser():
    login = input(" Enter login email-id: ")
    if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",login,re.IGNORECASE):
        print("valid")

    else:
        print("Email is invalid")
    while True:
        password = input(" Enter your Password: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
        elif re.search('[a-z]', password) is None: 
             print("Make sure your password has a small letter in it")


            
        if login in user and user[login] == password:
            print(" \nLogin successfullly!\n ")
            break    
        else:
            print("\nUser dosen't exist or wrong password!\n ")
            continue   
                        
while status != "q":

    displayMenu()











'''
user={}
status=""
import re
def displayMenu():
    status=input("Are you registered user?y/n Pree q to quit")
    if status == "y":
        oldUser() 
    elif status == "n":
            newUser()
            
def newUser():
    
    createLogin = input("Create login email-id: ")
    if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",createLogin,re.IGNORECASE):
        print("valid")

    else:
        print("Email is invalid")
    

    if createLogin in user:
        print("\nLogin email already exists!\n")
    else:
        createPwd = input("create Password: ")
        user[createLogin] = createPwd
        print("\nUser create\n")

def oldUser():
    login = input(" Enter login email-id: ")
    if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",login,re.IGNORECASE):
        print("valid")

    else:
        print("Email is invalid")
    password = input(" Enter your Password: ")

    if login in user and user[login] == password:
        print(" \nLogin successfullly!\n ")
    else:
        print("\nUser dosen't exist or wrong password!\n ")

while status != "q":
    displayMenu()

'''
























        















        
