import turtle

def H():
    
    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("blue")
    tar.width(5)
    tar.color("black")

    tar.speed(1)
    tar.penup()
    tar.fd(35)
    tar.pendown()
    tar.left(90)
    tar.fd(100)
    tar.bk(50)
    tar.left(90)
    tar.fd(50)
    tar.right(90)
    tar.fd(50)
    tar.bk(100)
    tar.penup()
    tar.right(90)
    tar.fd(80)
    tar.hideturtle()
    window.exitonclick()

H()
