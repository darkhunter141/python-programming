# tuple 
tp = (1,2,'tuple','string', 4.75, False)
print(tp,type(tp))
#tuple access is just like as list access
print(tp[2], tp[-1], tp[3])
# iteration 
for t in tp:
    print(t)
    
# tuple is immutable (its unchangable)
#tp[0] = 3
#print(tp) # this code will not work. because tuple is unchangable
# Note : we can change the tuple fully . we cant change individual value of tuple

# unpacking or multiple value assignment from the tuple
t = 1, 2, 3
x, y, z = t
print (x,y,z, sep = ' | ')

# dictionary 
dict = {'zero' : '0', 'one' : '1', 'two' : 2}
print(dict)
print(dict['zero'])
# length of dict 
print(len(dict))

#======= Modification====== 
dict['five'] = 5
print(dict) # add
del dict['five']
print(dict)

# Iteration key and value 
dic = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
for key, value in dic.items(): # ======  if i use (.key) then it will show only key || if i use .values then it will show every values of keys
    print(key, value, sep='=')

# sorted keys while iterate
for key in sorted(dic.keys()):
    print(key, dic[key])