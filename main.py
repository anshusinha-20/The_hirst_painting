"""
from turtle module, Turtle and Screen classes are imported
"""
from turtle import Turtle, Screen

"""tim object is created"""
tim = Turtle()
"""a turtle shape is provided """
tim.shape("turtle")
"""tim color is set to blue"""
tim.color("blue")

# """function to create a square"""
# def timMakeSquare():
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#     tim.right(90)
#     tim.forward(100)
#
# """function is called"""
# timMakeSquare()

"""function to create a dashed line"""
def timDashedLine():
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)

for i in range(10):
    timDashedLine()

"""screen object is created"""
screen = Screen()
"""screen will be exited upon a click"""
screen.exitonclick()
