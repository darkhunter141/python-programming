# Find the area of triangle 
def tri_area(a,b):

    return  0.5*a*b
a = int(input("enter your base: "))
b = int(input("enter your hight: "))

print("triangle area is : ",tri_area(a,b))
# convert tha ascii code into character 
def get_char(asc):
    return chr(asc)
asc = int(input("enter your ascii code :"))
print("the character of enter ascii code is :",get_char(asc))


# convert character into ascii code 
def get_ascii(char):
    return ord(char)
char = input("enter your character :")
print("the ascii code of the enter character is :",get_ascii(char))

# find the ascii number of a string value like name. 
def get_name_ascii(char):
    return ord(char)
char = input("enter your character :")
for i in char:
    v = get_name_ascii(i)
    print(v, end=' ')


# check the uppercase or lower case letter
ch = input("enter your letter :")
if ch.islower():
    print("the enter letter is lowercase")
else:
    print("the enter letter is uppercase")

# find an even and odd number 
def find_even_odd(num):
    if num%2 == 0: 
        print("your enter number is even ")
    else: 
        print("your entere number is odd ")
num = int(input("entere your number :"))
find_even_odd(num)

# convert celcious, farhenhit, kelvin scale 
class temp_convrt():

    def cel_farnt(self,temp):
       
        farn = (temp * 1.8) + 32
        return farn

    def farnt_cel(self,temp):
        temp = int(input("enter your temparature: "))
        cel = (temp - 32) * .5556
        return cel
temp = int(input("enter your temparature: "))

tmp = temp_convrt()
print(tmp.cel_farnt(temp))


# making a triangle (right side )
num = int(input("enter your desired number for rows: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

# another example
num = int(input("enter your desired number for pyramid: "))
k = 1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("*", end=" ")
    k = k+2
    print()
# pyramid 
num = int(input("enter your desired number for pyramid: "))

for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0, i + 1):
        print("*", end = " ")
    print()
