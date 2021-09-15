class MyClass: 
  
    # Hidden member of MyClass 
    __hiddenVariable = 0
    
    # A member method that changes  
    # __hiddenVariable  
    def add(self, increment): 
        self.__hiddenVariable += increment 
        print (self.__hiddenVariable) 
   
# Driver code 
myObject = MyClass()      
myObject.add(2) 
myObject.add(5) 
  
# This line causes error 
print (myObject.__hiddenVariable) 

# if we write this, then it will give us the output
print (myObject._MyClass__hiddenVariable) 
# here we learn that, it we want to call hidden data then we have to write the code => object + parant class + variable name
#We can access the value of hidden attribute by a tricky syntax as object._className__attrName:
