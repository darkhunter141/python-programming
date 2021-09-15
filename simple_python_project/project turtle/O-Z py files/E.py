import turtle

def E():
    
    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("blue")
    tar.width(5)
    tar.color("black")

    tar.speed(1)
    tar.fd(35)
    tar.bk(70)
    tar.left(90)
    tar.fd(100)
    tar.right(90)
    tar.fd(70)
    tar.penup()
    tar.right(90)
    tar.fd(50)
    tar.right(90)
    tar.pendown()
    tar.fd(70)
    tar.penup()
    tar.left(90)
    tar.fd(60)
    tar.left(90)
    tar.fd(80)
    tar.hideturtle()
    window.exitonclick()

E()
