import turtle

at = turtle.Turtle()

at.color("yellow", "red")

at.begin_fill()
for i in range(0,4):
    at.forward(100)
    at.left(90)
at.end_fill()
    
at.penup()
at.backward(200)
at.pendown()

at.begin_fill()
for i in range(0,4):
    at.forward(100)
    at.left(90)
at.end_fill()

turtle.done()