import re
def signUp():
        while True:
            first_name= (input("Enter  your first Name: "))
            if first_name == '':
                print("this field can't be blank")
                continue
            else: 
                break
        
        while True:
            last_name=(input("Enter  your last Name: "))
            if last_name == '':
                print("this field can't be blank")
                continue
            else:
                break

        while True:
            email = input("enter your emial address: " )
            if email == '':
                print("this field can't be blank")
            elif re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):#name er pore . nay na ?? match function (true/ false )
                break
            else:
                print("Email is invalid")
                continue
            
        while True:
            password = input("enter your password: " )
            if password == '':
                print("this field can't be blank")
            elif len(password) < 8:
                print("Make sure your password is at lest 8 letters")
            elif re.search('[0-9]{2}',password) is None:
                print("Make sure your password has a number in it")
            elif re.search('[A-Za-z]',password) is None: 
                print("Make sure your password has a capital letter in it")
            elif re.search('[^a-zA-Z0-9]', password) is None:
                print("Make sure your password has a symbol in it")
            else:
                print("Your password seems fine")
                break
        while True:
            re_password = input("Re-enter your password: " )
            if re_password == '':
                print("this field can't be blank")
            if len(re_password) < 8:
                print("Make sure your password is at lest 8 letters")
            elif re.search('[0-9]{2}',re_password) is None:
                print("Make sure your password has a number in it")
            elif re.search('[A-Z]',re_password) is None: 
                print("Make sure your password has a capital letter in it")
            elif re.search('[^a-zA-Z0-9]', re_password) is None:
                print("Make sure your password has a symbol in it")
            elif re_password == password:
                print("password match")
            else:
                print("password does not match")
                break             


signUp()
