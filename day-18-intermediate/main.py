from turtle import Turtle, Screen, colormode
import random
colormode(255)
joel = Turtle()
joel.shape("turtle")
joel.color("green")
joel.speed("fastest")
joel.pensize(1)

directions = [0, 90, 180, 270]
my_tuple = (21, 13, 250)
angle = 2
while angle <= 360:
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    joel.pencolor((a, b, c))
    joel.circle(100)
    joel.left(3)
    angle += 2

screen = Screen()
screen.exitonclick()
