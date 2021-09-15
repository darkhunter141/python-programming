import turtle

def P():

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
    tar.fd(55)
    tar.right(90)
    tar.fd(70)

    tar.penup()
    tar.left(90)
    tar.forward(50)
    tar.left(90)
    tar.fd(90)
    tar.pendown()
    window.exitonclick()

P()