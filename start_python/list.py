# creating a list 


a = [1, 5, 6, "s", 10]
print(a)
#========= by indexing we can print every element individually =======
print(a[0])
print(a[0:3]) #last number doesn't exist in python
print(a[1:5])# slicing operator 
# ===== nested list ======== 

b = [1, 5, 6, [10, 7, 8,], "baset"]
print(b)
print(b[2])
print(b[3][2])  # nested lists value printing 

#======== NEGETIVE INDEXING ============= #
print(a[-1])

print(a[:-1])
print(a[2:])#slicing


#====== List Unpacking ======= # 
x = ["baset", "shuvro", "orpon"]
d,e,f = x
print(d)
y = [1,5,6,8,3,6,69,85,89]
m,*n,l = y
#======== assign multiple value within one variable === #
print(n)

# ========== Update add delete ============= #
p = [23,7,75,10]
p[3] = 5
#=== change========= 
print(p)
p[0:4]=[5,7,23,75]
#== change multiple value ======= #
print(p)
#add one value
p.append(10)
print(p)

# add multiple value 

p.extend(["baset",475,3])
print(p)
#========= Inset ========== #
p.insert(4,2)# 1st place is location and 2nd one is value
print(p)

p[5:3]=[11,12,13]
print(p)

#======= Delete ============#

del p[4]
print(p)
del p[7:9]
print(p)

#====== Remove ========== #
p.remove(475)
print(p)

# ==== Clear ===== #
a.clear()
print(a)

sp = [1,10,45,6,2,84,6]
print(sp.index(45))#=== values index nmbr === # 
print(sp.count(6))#=== count values == # 
#== sorting ==== #
sp.sort()
print(sp)
# === reverse ===== 
sp.reverse()
print(sp)
#======== list length ==== # 
print(len(sp))
# ===== list max min sorted sum ===== # 
print(max(sp))
print(min(sp))
print(sum(sp))
print(sorted(sp))

# == is here any item in this list ? :) =====# 
print(4 in sp)
print(1 in sp)
#====== using for loop in list ========== #
bps = [2 ** x for x in range(7)]
print(bps)
#======= List Comprehension========= using for loop ==== #   
mylist = []
for letter in 'shuvro':
	mylist.append(letter)
print(mylist)

# 2nd way #
my_list = [letter for letter in 'baset']
print(my_list)

nmlist = [letter for letter in '4568765']
print(nmlist)

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

nmlist = [int(letter) for letter in '4568765']
print(nmlist)