import turtle

def drawing():
    
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.width(10)
    brad.right(150)
    brad.fd(150)
    brad.back(150)
    brad.fd(150)
    brad.left(150)
    brad.fd(150)
    brad.goto(60,30)
    brad.sety(-10)
    brad.setheading(180)
    brad.home()
    brad.circle(30)
    brad.dot("blue")
    brad.speed(1)
    brad.fd(150)
    brad.pen("yellow")
    brad.pencolor("blue")
    brad.fd(150)
    brad.fillcolor("green")
    brad.fd(50)
    brad.fillcolor("blue")
    brad.fd(50)
    #brad.shape("arrow" /"turtle"/ "circle"/"square"/"triangle"/"classic")
    window.exitonclick()


    

drawing()

