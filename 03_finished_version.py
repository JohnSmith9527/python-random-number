import turtle
turtle.mode("logo")
turtle.shape("turtle")

size=50
length=150

turtle.pu()
turtle.goto(20,30)
turtle.pd()
turtle.pencolor("green")
turtle.forward(length)
turtle.dot(size)

turtle.pu()
turtle.goto(0,-10)
turtle.pd()
turtle.pencolor("red")
turtle.forward(length)
turtle.dot(size)


turtle.pu()
turtle.goto(90,80)
turtle.pd()
turtle.pencolor("orange")
turtle.forward(length)
turtle.dot(size)


turtle.pu()
turtle.goto(-30,50)
turtle.pd()
turtle.pencolor("blue")
turtle.forward(length)
turtle.dot(size)

turtle.hideturtle()
turtle.done()
