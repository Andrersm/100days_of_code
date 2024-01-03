from turtle import Turtle, Screen

joel = Turtle()
screen = Screen()


def move_forwards():
    joel.forward(10)


def mmove_right():
    joel.right(10)


def move_left():
    joel.left(10)


def move_backwards():
    joel.backward(10)


def reset():
    joel.home()
    joel.clear()


screen.listen()
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=mmove_right, key="d")
screen.onkeypress(fun=move_left, key="a")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=reset, key="c")
screen.exitonclick()