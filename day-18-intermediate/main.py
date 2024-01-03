import colorgram

colors = colorgram.extract('obra_66205.jpg', 7)

from turtle import Turtle, Screen, colormode
import random

colormode(255)
joel = Turtle()
joel.shape("arrow")
joel.color("green")
joel.pensize(20)
number_x = -150
number_y = 0
i = 0
color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)
x = 0
while x < 10:
    i = 0
    while i <= 10:
        joel.teleport(x=number_x, y=number_y,)
        joel.pencolor(random.choice(color_list))
        joel.forward(1)
        number_x += 30
        i += 1
    number_x = -150
    x += 1
    number_y += 30
    joel.teleport(x=number_x, y=number_y)
screen = Screen()
screen.exitonclick()