import turtle

def D():
    
    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("blue")
    tar.width(5)
    tar.color("black")

    tar.speed(1)
    tar.left(180)
    tar.fd(35)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.right(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(35)
    tar.penup()
    tar.bk(35)
    tar.right(180)
    tar.fd(20)
    window.exitonclick()

D()
