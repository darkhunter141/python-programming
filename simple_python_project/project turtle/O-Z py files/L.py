import turtle

def L():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("blue")
    tar.width(5)
    tar.color("black")

    tar.speed(1)
    tar.penup()
    tar.fd(40)
    tar.left(180)
    tar.fd(35)
    tar.right(90)
    tar.fd(100)
    tar.pendown()
    tar.bk(100)
    tar.right(90)
    tar.fd(70)
    tar.penup()
    tar.fd(20)
    window.exitonclick()
L()
