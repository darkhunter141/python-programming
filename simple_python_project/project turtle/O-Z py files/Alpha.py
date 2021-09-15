import turtle

tar = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("#B0BF1A")
tar.shape("turtle")
tar.width(5)
tar.color("green")

j = "jJ"
a = "Aa"
class alpha:

    def J(self):
        tar.penup()
        tar.setposition(60, 0)
        tar.pendown()
        tar.left(90)
        tar.penup()
        tar.fd(100)
        tar.pendown()
        tar.right(90)
        tar.fd(65)
        tar.right(90)
        tar.fd(100)
        tar.right(90)
        tar.fd(50)
        tar.right(90)
        tar.fd(35)
        #tar.hideturtle()
        window.exitonclick()
        #tar.getscreen()._root.mainloop()


    def A(self):
        tar.penup()
        tar.setposition(60, 0)
        tar.pendown()
        tar.left(75)
        tar.fd(100)
        tar.right(150)
        tar.fd(100)
        tar.bk(30)
        tar.right(105)
        tar.fd(36.23)
        #tar.hideturtle()
        window.exitonclick()
        #tar.getscreen()._root.mainloop()


c = alpha()
i = str(input("your name: "))
for p in i:
    if p in j:
        print(c.J())
    elif p in a:
        print(c.A())
    else:
        print("Sorry")


