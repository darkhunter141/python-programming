import turtle

def N():
    
    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("blue")
    tar.width(5)
    tar.color("black")
    tar.speed(1)

    tar.left(90)
    tar.fd(100)
    tar.right(145)
    tar.fd(122)
    tar.left(145)
    tar.fd(100)
    tar.penup()
    tar.backward(100)
    tar.right(90)
    tar.fd(20)
    tar.pendown()
    window.exitonclick()

N()
