import turtle

def draw_sq():
    brad = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor("red")
    window.setup(width=900, height=700)

    brad.shape("turtle")
    brad.color("green")
    brad.speed(1)
    brad.width(5)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()

draw_sq()
