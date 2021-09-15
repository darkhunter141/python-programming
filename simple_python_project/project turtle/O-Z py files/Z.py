import turtle

def Z():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("red")
    tar.width(5)
    tar.color("green")

    tar.speed(1)
    tar.left(90)
    tar.penup()
    tar.fd(100)
    tar.right(90)
    tar.pendown()
    tar.fd(70)
    tar.right(135)
    tar.forward(135)
    tar.left(135)
    tar.forward(70)
    tar.penup()
    tar.fd(40)
    tar.pendown()
    window.exitonclick()
Z()



