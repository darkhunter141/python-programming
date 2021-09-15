import turtle

def R():

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
    tar.fd(70)
    tar.right(90)
    tar.fd(50)
    tar.right(90)
    tar.fd(70)
    tar.bk(20)
    tar.left(135)
    tar.fd(70)
    tar.penup()
    tar.left(45)
    tar.fd(30)
    tar.pendown()
    window.exitonclick()
R()