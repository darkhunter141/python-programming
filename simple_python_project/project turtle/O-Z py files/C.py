import turtle

def C():

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
    tar.penup()
    tar.fd(100)
    tar.right(90)
    tar.pendown()
    tar.fd(35)
    tar.penup()
    tar.bk(45)
    tar.right(180)
    tar.fd(20)
    #tar.hideturtle()
    window.exitonclick()

C()
