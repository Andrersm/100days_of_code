from turtle import Turtle, Screen
import random

joel = Turtle()
joel.shape("turtle")
joel.color("green")
number = 360
div = 3
color = ["red", "blue", "yellow", "orange", "purple"]
while div < 10:
    for _ in range(div):
        joel.forward(100)
        joel.right(number/div)
    joel.color(random.choice(color))
    div += 1

screen = Screen()
screen.exitonclick()