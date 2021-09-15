import turtle

def U():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("red")
    tar.width(5)
    tar.color("green")

    tar.speed(1)
    tar.left(90)
    tar.penup()
    tar.fd(122)
    tar.right(180)
    tar.pendown()
    tar.fd(78)

    for i in range(22):
        tar.fd(6)
        tar.left(8)

    tar.left(6)
    tar.fd(88)
    tar.penup()
    tar.right(180)
    tar.fd(122)
    tar.left(88)
    tar.fd(30)
    tar.pendown()
    window.exitonclick()
U()