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

# """function to create a dashed line"""
# def timDashedLine():
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#
# for i in range(10):
#     timDashedLine()

"""function to create different sizes i.e from triangle to decagon"""
def timMakePolygon(angle, color):
    tim.color(color)
    tim.forward(100)
    tim.right(angle)

colors = ["#ade8f4", "#90e0ef", "#48cae4", "#00b4d8", "#0096c7", "#0077b6", "#023e8a", "#03045e"]
count = 0
for i in range(3, 11):
    color = colors[count]
    for j in range(0, i):
        timMakePolygon(360/i, color)
    count += 1

"""screen object is created"""
screen = Screen()
"""screen will be exited upon a click"""
screen.exitonclick()
