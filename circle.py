import turtle

def drawsquare(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def drawcircle():
    window=turtle.Screen()
    window.bgcolor("YELLOW")

    rob= turtle.Turtle()
    rob.shape("turtle")
    rob.color("RED")
    for i in range(1,37):
        drawsquare(rob)
        rob.right(10)

    window.exitonclick()

drawcircle()
