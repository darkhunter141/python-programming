import turtle

def M():
    
    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("blue")
    tar.width(5)
    tar.color("black")
    tar.speed(1)

    tar.left(90)
    tar.fd(100)
    tar.right(150)
    tar.fd(45)
    tar.left(120)
    tar.fd(45)
    tar.right(150)
    tar.fd(100)
    tar.penup()
    tar.left(90)
    tar.fd(20)
    tar.pendown()
    window.exitonclick()

M()
