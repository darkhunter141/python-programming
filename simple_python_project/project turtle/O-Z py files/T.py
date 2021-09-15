import turtle

def T():

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
    tar.fd(35)
    tar.bk(70)
    tar.penup()
    tar.right(90)
    tar.fd(100)
    tar.left(90)
    tar.fd(100)
    tar.pendown()
    window.exitonclick()
T()