from turtle import*
from random import randint
bgcolor("black")

x=1
speed(0)
shape("classic")

while x<400:
    r=randint(0,255)
    g=randint(0,200)
    b=randint(50,200)
    colormode(255)
    pencolor(r,g,b)
    forward(50+x)
    right(90.99)
    x=x+1
exitonclick()
