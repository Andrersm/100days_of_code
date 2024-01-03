from turtle import Turtle, Screen
import random

joel = Turtle()
joel.shape("turtle")
joel.color("green")
number = 10
for _ in range(30):
    joel.forward(5)
    joel.teleport(x=number, y=0, fill_gap=True)
    number += 10
    print(number)

screen = Screen()
screen.exitonclick()