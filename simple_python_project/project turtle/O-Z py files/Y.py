import turtle

def Y():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("red")
    tar.width(5)
    tar.color("green")

    tar.speed(1)
    tar.left(90)
    tar.penup()
    tar.fd(50)
    tar.pendown()
    tar.left(35)
    tar.fd(50)
    tar.bk(50)
    tar.right(70)
    tar.fd(52)
    tar.back(52)
    tar.right(145)
    tar.forward(50)
    tar.penup()
    tar.left(90)
    tar.fd(45)
    tar.pendown()
    window.exitonclick()
Y()



