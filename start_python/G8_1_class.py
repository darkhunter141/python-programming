class Coachng:
    st_name = '' # global variable/ class variable
    st_class = ''

    def details(self):
        print(self.st_name, self.st_class)
    
    def details_with_address(self, address):
        print(self.st_name, self.st_class)
        print(address)

c = Coachng()
c.details
c.st_name = "shuvro"
c.st_class = "hons"
c.details
c.details_with_address("dhaka")
print(type(c))

# Contrusctor method 
class Person:
    def __init__(self, name, age):# 1st method called autometically that is init method
        self.name = name
        self.age = age

    def details(self):
        print(self.name, self.age, sep = '|')
shuvro = Person('shuvro', 27)
shuvro.details()
print( shuvro.name, shuvro.age)
    
#creating more than 1 object
class Person:
    def __init__(self, name, age):# 1st method called autometically that is init method
        self.name = name
        self.age = age

    def details(self):
        print(self.name, self.age, sep = '|')

people_list = []
for x in range(0,3):
    prsn = Person("Person " +str(x), 30+x)
    people_list.append(prsn)
    #people_list += [prsn]
for x in people_list:
    x.details()
# print(people_list[0:]) #?????????


#========= attribute value modification
chnge = Person(name='baset', age=25)
chnge.details()

chnge.name="shuvro"
chnge.details()

#========== Lifecycle ====== 
class X: 
    def __init__(self, name):
        self.name = name
        print(self.name + " created")
    def __del__(self):
        print (self.name + " is destroyed ")

x = X('X')
y = X('Y')
print("hello world")

def hello():
    x = X('hello _ X')
    y = X('hello _y')
hello()

#============ Inheritence =========
class Math:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y

class MathExtended1(Math):
    def __init__(self, x , y):
        super().__init__(x,y)
    
    def subtract(self):
        return self.x - self.y

math_ext_obj = MathExtended1(10,5)
print( math_ext_obj.sum() )

#=========== Multiple Inheritance ========== 
class MathExtra:
    def division(self, x, y):#===== without __init__ method
        return x / y

class MathExtended2(MathExtended1, MathExtra): #child class
    def __init__(self, x , y):
        super().__init__(x, y)

    def multiplication(self):
        return self.x * self.y

    

math_ext2 = MathExtended2(10,2)
print("Sum", str(math_ext2.sum()) )
print( "Subtract", str(math_ext2.subtract()))
print ("muliplication", str(math_ext2.multiplication()))
print( "division", str(math_ext2.division(x=math_ext2.x, y = math_ext2.y)))
    
    
#print( "division", str(math_ext2.division(x = 10, y = 5)))#= no __init__ method . so we have to call a keyword argument 


#=======Method Override=============
class Math:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y

    def sum(self):#Method Override
        return self.x + self.y + 75

    def show_all(self):
        print("sum of child class: "+ str(super().sum()))
        print("sum of override : "+ str(self.sum()))
