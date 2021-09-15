import turtle

def K():
    
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
    tar.pendown()
    tar.fd(100)
    tar.bk(50)
    tar.right(45)
    tar.fd(70)
    tar.bk(70)
    tar.right(90)
    tar.fd(70)
    tar.penup()
    tar.left(45)
    tar.fd(10)
    window.exitonclick()

K()
