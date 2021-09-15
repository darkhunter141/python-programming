import turtle

def V():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("red")
    tar.width(5)
    tar.color("green")

    tar.speed(1)
    tar.penup()
    tar.fd(20)
    tar.pendown()
    tar.left(112)
    tar.fd(100)
    tar.bk(100)
    tar.right(45)
    tar.fd(102)
    tar.right(158)
    tar.penup()
    tar.fd(94)
    tar.left(90)
    tar.fd(20)
    tar.pendown()
    window.exitonclick()
V()



