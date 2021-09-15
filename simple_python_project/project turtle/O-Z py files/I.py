import turtle

def I():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("red")
    tar.width(5)
    tar.color("green")

    tar.speed(1)
    tar.left(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(5)
    tar.bk(10)
    tar.fd(5)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(5)
    tar.bk(10)
    tar.penup()
    tar.bk(10)
    tar.right(180)
    tar.fd(15)
    window.exitonclick()


I()