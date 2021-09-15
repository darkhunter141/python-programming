import turtle

brad = turtle.Turtle()
brad.shape("turtle")
window = turtle.Screen()
window.bgcolor("#B0BF1A")

for i in range(3):

    brad.width(5)
    brad.color("green")
    brad.forward(100)
    brad.right(360/3)

window.exitonclick()

