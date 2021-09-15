import turtle

def Q():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    #window.bgcolor("red")
    tar.width(5)
    tar.color("green")
    tar.speed(1)

    tar.left(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.bk(70)
    tar.left(130)
    tar.fd(10)
    tar.bk(20)
    tar.penup()
    tar.fd(10)
    tar.left(50)
    tar.fd(30)
    tar.pendown()
    window.exitonclick()

Q()