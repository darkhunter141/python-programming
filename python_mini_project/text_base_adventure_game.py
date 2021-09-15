# import time module
import time
# make list for True
true = ["T", "t", "True"]
# make list for False
false = ["F", "f", "False"]
#Storing the correct answers
correct = 0 

#Storing the user's name
name = input ("What's your name: ") 

print(f"\nOK,{ name } , let's get started. Remember, the following answers are only True or False. Please give an answere typing 't' or 'f' ")
# delay time
time.sleep(2)

# question number 1 for the user
print("\n Python is an object oriented language.")
choice = input(">>> ")
# condition for user ans.
if choice in true:
    #If correct, the user gets one point
  correct += 1 
else:
  correct += 0
  
print("\nHtml is a programming language.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0  

print("\n Python is low level programming language.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0 
  
print("\n python is best for Data Science and Big data analysis.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0  
  
print("\n MatplotLib is very important tool for data analysis.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0
  
print("\n in python there is no polymorphism method.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0
    
# Print the final result
print(f"\nYou're finished,  {name} You got, {correct}, out of 6 correct.")