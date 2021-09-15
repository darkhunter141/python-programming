import Alpha

j = "jJ"
a = "Aa"

c = Alpha.alpha()


i = str(input("your name: "))

for p in i:
    if i in j:
        print(c.J(),end=" ")
        #Alpha.setposition(60, 60)
    elif i in a:
        print(c.A(),end=" ")
        #Alpha.setposition(60, 60)
    else:
        print("sorry")

#Alpha.getscreen()._root.mainloop()