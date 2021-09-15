import turtle

def X():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("purple")
    tar.width(5)
    tar.color("green")

    tar.speed(1)
    tar.penup()
    tar.fd(20)
    tar.pendown()
    tar.left(90)
    tar.penup()
    tar.fd(70)
    tar.pendown()
    tar.right(135)
    tar.forward(100)
    tar.left(135)
    tar.penup()
    tar.forward(70)
    tar.pendown()
    tar.left(135)
    tar.forward(100)
    tar.penup()
    tar.left(135)
    tar.fd(100)
    tar.pendown()
    window.exitonclick()
X()



