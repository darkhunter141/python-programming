a = input("enter ur 1st number: ")
b = input("enter ur 2nd number: ")
c = input("enter ur 3rd number: ")

if (a>b and a<c):
    print(" {} is a middle number".format(a))
elif (a<b and a>c):
	print("{} is a middle number ".format(a))
elif(b>a and b<c):
    print("{} is a middle number ".format(b))
elif(b<a and b>c):
    print("{} is a middle number".format(b))
elif(c>a and c< b):
    print("{} is a middle number ".format(c))
else:
    print("{} is a middle number".format(c))