from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("blue")


def timMakeSquare():
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)
    tim.right(90)
    tim.forward(100)


timMakeSquare()

screen = Screen()
screen.exitonclick()
