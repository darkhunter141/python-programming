n = int(input("enter your number: "))
# 1st condition 
if n < 30:
    print("you are fail")
    # 1st inner statement
    if n > 20:
        print(" u will get a chance ")
    elif n > 10:
        print(" u are dull")
    else:
        print(" u are too dull ")
# 2nd condition 
elif n < 60:
    print(" u pass")
    # 2nd inner statement
    if n > 50:
        print(" u are good")
    else:
        print(" u are not bad")
#3rd condition
else:
    print(" welcome to our group")
    #3rd inner statement
    if n < 75:
        print(" try more ")
    elif n < 90:
        print(" well done better luck for the next time")
    else: 
        print(" congrats u are selected for ur briliant reslt")