# welcome to function 
def welcome(name):
    print("welcome {}".format(name))

welcome('shuvro')
welcome('baset')

# positional argument
def prsn_detail(name,age,devision):
    print(name,age,devision, sep='|')
prsn_detail('baset',27,'dhaka')
prsn_detail('ratri',23,'jessore')

# argument order doesn't matter / keyword argument 
prsn_detail('shuvro', age=27, devision = 'dhaka') 
prsn_detail(age = 27, name = 'shuvro', devision= 'dhaka')

# Default value 
def cstmr_details(name, age, country='bangladesh'): # default value maintain sequence from last side
    print(name,age,country, sep = '|')
cstmr_details('shuvro',25)

#return value
def square(num):
    return num * num
print(square(3),square(5.5), sep = '|')

# name concate
def name(first_name, last_name):
    return first_name + " " + last_name
print( name('shuvro','baset'))

# Optional argument
def get_name(first_name, last_name, middle_name=''):
    complete_name = first_name
    if middle_name:
        complete_name += ' ' + middle_name
    complete_name += ' ' + last_name
    return complete_name
print( get_name('shuvro', 'baset'))
print( get_name('shuvro','baset', 'rudro') )

# reference type parameter 
nm = 50
def new_num(nm):
    nm += 25
    print( "inner number : {}".format(nm))

new_num(nm)
print( ' 1st_number :' + str(nm))

# list, dictionary (this reference type parameter will effect )
num_list = [1,2,3,4,5]
num_dict = { 'one':1, 'two' : 2, 'three' : 3}

def change_num_list(list,dict):
    del list[0]
    list[-1] = 75

    del dict['one']
    dict['three'] = 23
    print("Inner List : ", list)
    print("Inner dict: ", dict)

print("before")
print(" Outer list: ", num_list)
print( "Outer dict: ", num_dict)
change_num_list(list=num_list, dict= num_dict)
print("after")
print("outer List: ", num_list)
print("outer List: ", num_dict)

#=== Arbitrary number of arguments (unknown parameter)
def students(*students_name):
    print(students_name, type(students_name))
    for students in students_name:
        print (students)

students('shuvro', 'baset', 'rudro', 'dipto')
students()
students('pushpo')

# Positional and arbitrary arguments mixing
def team(cap, *member):
    print('captain', cap)
    print('others', member)
team('shuvro', 'forhad', 'rubel', 'shemanto')

# Arbitrary keyword arguments (** dictionary )
def team2(cap,**others):
    print('captain',cap)
    print('other', others)
team2(cap= 'shuvro', sec_cap = 'baset', third_cap = 'shemanto')

#====== LAMBDA ======= #
# anonymous or Inline function
 
add_numbers = lambda a,b : a + b 
print( add_numbers(2,3))

man = lambda name: "we love: " + name
print(man('bangladesh'))