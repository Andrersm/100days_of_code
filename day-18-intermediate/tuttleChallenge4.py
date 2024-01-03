from turtle import Turtle, Screen
import random

joel = Turtle()
joel.shape("turtle")
joel.color("green")
joel.speed("fastest")
joel.pensize(10)
cores = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'magenta', 'black', 'brown', 'gray']
directions = [0, 90, 180, 270]

for _ in range(100):
    joel.color(random.choice(cores))
    joel.forward(30)
    joel.setheading(random.choice(directions))
    
screen = Screen()
screen.exitonclick()