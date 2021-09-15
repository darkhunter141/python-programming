          # ==========condition 

num = 50
if num % 2 == 0:
    print("even number")

         #====input function - even/ odd

a = int(input("enter ur number: "))
if(a % 2 == 0):
    print("the enter number is even")
else:
    print("the enter number is odd")


         # if-elif-else chained condition
num = int(input("enter a number: "))
if num == 50:
    print("half century")
elif num ==100:
    print("century")
elif num > 100:
    print("century +")
else:
    print("unknown number")

         # logical operator and/or
nm = 1
if nm >=3 or nm > 0:
    print("condition is true")

         #compare string
name1 = "Shuvro"
name2 = "shuvro"
if name1 == name2: # if name1.lower()== name2.lower() then name match
    print("same name")
else:
    print("name doesn't match") # case problem. 

         # not equals to 

name = "unknown person"
if name != "shuvro":
    print(name)

         ### Loop #####

     #while loop # 

x = 1
while x <=5:
    print (x)
    x += 1

#=======infinity loop # 
# 


#======== break loop # 
# b = 1
# while True:
#     print(b)
#     b += 1
#     if b > 10:
#         break

       # continue loop # 
x = 0
while x < 20:
    x += 1
    if x % 2 == 0:        
        continue
    print(x)


        # For loop # 
sum = 0
for num in range(1,11):
    print(num)
    sum += num
print("sum is {sum}".format(sum=sum))

           # for loop for string # 

name = "shuvro"
for char in name:
    print(char)