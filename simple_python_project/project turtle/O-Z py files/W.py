import turtle

def W():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("red")
    tar.width(5)
    tar.color("green")
    tar.speed(1)

    tar.left(95)
    tar.fd(100)
    tar.bk(100)
    tar.right(15)
    tar.fd(102)

    tar.right(160)
    tar.fd(100)
    tar.left(165)
    tar.forward(100)
    tar.penup()
    tar.right(175)
    tar.fd(100)
    tar.left(90)
    tar.fd(20)
    tar.pendown()
    window.exitonclick()
W()



