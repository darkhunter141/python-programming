#===== Class variable and Instance Variable details 
class prj:
    st = 70 #class variable
    def __init__(self, name):
        self.name = name#Instance variable
# Instantiation 
prj1 = prj('shuvro')
prj2 = prj('baset')

print(prj1.name, prj2.name)# Accessing Instance variable
print(prj1.st, prj2.st)# Accessing class variable

#====== changing class variable
prj.st = 75# change value of class variable/ parmenantly change
print(prj.st, prj2.st)
prj1.__class__.st = 7# this is the best way to change a class variable fixed
print(prj1.st, prj2.st)

#==========value change using object bt .......
# if we change variable by calling object then it will change only that object. 
# bt actual class variable as like as same
prj1.st = 23
print(prj1.st, prj2.st)

#==========8.2===========#
# ---------- ('==' vs 'is' operator)
x = [1,2,3]
xx = x

print(x == x)
print(x is xx)

y = list(x)
print(x == y)
print(x is y)

#====== 8.2======
#====== OOP class to string =====
class prsn:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.__class__.__name__} class, obj name: {self.name}'

p1 = prsn("shuvro")
p2 = prsn("baset")
print(p1)
print(p2)