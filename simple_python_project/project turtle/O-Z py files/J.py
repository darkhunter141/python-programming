import turtle

def J():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("red")
    tar.width(5)
    tar.color("green")

    tar.speed(1)
    tar.penup()
    tar.left(180)
    tar.fd(35)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.pendown()
    tar.fd(70)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(60)
    tar.right(90)
    tar.fd(35)
    tar.penup()
    tar.bk(35)
    tar.right(90)
    tar.fd(70)
    tar.pendown()
    window.exitonclick()
J()