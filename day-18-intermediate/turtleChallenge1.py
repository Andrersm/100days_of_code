from turtle import Turtle, Screen
import random

joel = Turtle()
joel.shape("turtle")
joel.color("green")
for _ in range(4):
    joel.forward(100)
    joel.right(90)

screen = Screen()
screen.exitonclick()