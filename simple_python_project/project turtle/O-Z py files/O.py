import turtle

def O():

    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("red")
    tar.width(5)
    tar.color("green")
    tar.speed(1)
    for i in range(36):
        tar.fd(9)
        tar.left(10)
    tar.penup()
    tar.fd(90)
    tar.pendown()
    window.exitonclick()
O()
