import turtle

def A():
    
    
    tar = turtle.Turtle()
    tar.shape("turtle")
    window = turtle.Screen()
    window.bgcolor("blue")
    tar.width(5)
    tar.color("black")
    
    tar.speed(1)
    tar.penup()
    tar.left(180)
    tar.fd(35)
    tar.right(108.29)
    tar.pendown()
    tar.fd(105.95)
    tar.right(141.42)
    tar.fd(105.95)
    tar.bk(35)
    tar.right(108.29)
    tar.fd(46.88)
    tar.penup()
    tar.left(90)
    tar.fd(33.04)
    tar.left(90)
    tar.fd(78.44)
    tar.pendown()
    window.exitonclick()
    
A()
