n = int(input("enter your desire factorial number"))
fact = 1
  
for i in range(1,n+1): 
    fact = fact * i
    print(fact)
      
print ("The factorial of {} is : ".format(n),end="") 
print (fact) 