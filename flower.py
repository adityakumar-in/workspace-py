import turtle

at = turtle.Turtle()
at.speed(20)

at.color("yellow", "red")

at.begin_fill()
for i in range(0, 72) :
    at.forward(200)
    at.left(155)
at.end_fill()

at.penup()
at.backward(600)
at.pendown()

at.begin_fill()
for i in range(0, 72) :
    at.forward(200)
    at.left(155)
at.end_fill()

turtle.done()