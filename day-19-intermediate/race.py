from turtle import Turtle, Screen
import random
screen = Screen()
joel = Turtle()

joana = Turtle()
jessica = Turtle()
joberval = Turtle()
juvanelson = Turtle()

joel.shape("turtle")
joel.color("red")

joana.shape("turtle")
joana.color("blue")

jessica.shape("turtle")
jessica.color("green")

joberval.shape("turtle")
joberval.color("yellow")

juvanelson.shape("turtle")
juvanelson.color("purple")


def inicial():
    joel.penup()
    joel.goto(-450, 100)
    joel.pendown()

    joana.penup()
    joana.goto(-450, 50)
    joana.pendown()

    jessica.penup()
    jessica.goto(-450, 0)
    jessica.pendown()

    joberval.penup()
    joberval.goto(-450, -50)
    joberval.pendown()

    juvanelson.penup()
    juvanelson.goto(-450, -100)
    juvanelson.pendown()


bet = screen.textinput(title="Escolha um cor", prompt="Escolha uma cor: ")

winner = ""
def start_race():
    winner = ""
    for i in range(1000):
        joel.forward(random.randint(1, 90))
        joana.forward(random.randint(1, 10))
        jessica.forward(random.randint(1, 10))
        joberval.forward(random.randint(1, 10))
        juvanelson.forward(random.randint(1, 10))
        if joel.xcor() > 450:
            print("joel ganhou")
            winner = "red"
            break
        elif joana.xcor() > 450:
            print("joana ganhou")
            winner = "blue"
            break
        elif jessica.xcor() > 450:
            print("jessica ganhou")
            winner = "green"
            break
        elif joberval.xcor() > 450:
            print("joberval ganhou")
            winner = "yellow"
            break
        elif juvanelson.xcor() > 450:
            print("juvanelson ganhou")
            winner = "purple"
            break
    if winner == bet:
        print("você ganhou")
    else:
        print("você perdeu")
    return


inicial()
screen.listen()
screen.onkey(start_race, "space")
screen.exitonclick()