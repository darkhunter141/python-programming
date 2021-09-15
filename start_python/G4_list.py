#========== declare a list with 3rd brackets 
list1 = ['baset', 'shuvro', 'writer']
print(list1)
print(list1[1])

#============= mixed list (with defferent type of data)
list2 = ['shuvro', 75, 4.1, 23, False]
print(list2)
print(list2[-1])

#================== Empty list 
list3 = []

mat = [[1,2,3,4],[4,5,8,6],[5,6,8,3]]
for x in mat:
    for y in x:
        print(y, end = ' ')# stop printing in new line . 
    print()

# ==============list iteration by for loop 
car = ['bike','r15','xixer',]
for x in car:
    print(x)
    if x == 'r15':
        print("r15 is the best bike")

#============== sum of the list numbers
sum = 0
list3 = [1,5,7,9,6,4]
for y in list3:
    sum += y
print("sum is : {}".format(sum))

# =============sum ignore string value
sum = 0
list3 = [1,5,7,'asd',6,4]
for y in list3:
    if type(y) == int:
        sum += y
print("sum is : {}".format(sum))

#=================== list modification changing value 
list4 = ["shuvro", 75, 23, 4.75, False]
list4[0] = "baset"
print(list4)

# ============add item
list4.append("hehe")
print(list4)

#============== adding list specific position
list4.insert(2, "add")
print(list4)

#========== delete list item
del list4[3]
print(list4)

#============= delete last item
last_list4 = list4.pop()
print(list4, "\n", last_list4)

#=========== remove list item by value 
rmve = [1,2,3,4,5,6,8,5,6]
print(rmve)
rmve.remove(6)
print(rmve)# remove 1st 6

#============= splitting string into list items
import re
name = "baset, shuvro, dipto"
name_list = re.split(',',name)
print(name_list)

#================= convert a list into string 
list2str = ['here', 'is', 'converting', 'string']
convrt_str = ' '.join(list2str)
print(convrt_str)

#============= sorting ( alphabetically )
list2str.sort()
print(list2str)
list2str.sort(reverse=True)
print(list2str)

# ================reverse list 
rmve.reverse()
print(rmve)

#===========length of list 
print(len(rmve))

#===================checking a value in the list 
rmve = [1,2,3,4,5,6,8,5,6]
if 1 in rmve:
        print("yes it is")

