# Matching 2 list and appending in another list without similar value

a = [1,1,2,3,4,8,13,23,4,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

c = []

for i in a:
    if i in b:
        if i in c:
            c.remove(i)
        c.append(i)
print(c)

# lcm finder
a = int(input("enter your number: "))
lcm = []
i = 1
for i in range(i,a+1):
    if a % i == 0:
        lcm.append(i)
    i = i+1;
print(lcm)

# dictionary adding
dic1 = {1:10, 2: 20}
dic2 = {3:30, 4: 40}
dic3 = {5:50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)



# fibonacci
i = 0
j = 1
k = [0,1]
g = int(input("how many number you want to generate a fibonacci series: "))
for m in range(g-2):
    res = i+j
    i = j
    j = res
    k.append(res)
print(k)

# fibonacci 2
i = int(input("Enter your first initial point: "))
j = int(input("Enter your second initial point: "))
k = [i,j]
g = int(input("how many number you want to generate a fibonacci series: "))
for m in range(g-2):
    res = i+j
    i = j
    j = res
    k.append(res)
print(k)