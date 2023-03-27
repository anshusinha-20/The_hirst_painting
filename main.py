"""
from turtle module, Turtle and Screen classes are imported
"""
import turtle
from turtle import Turtle, Screen

"""random module is imported"""
import random

"""tim object is created"""
tim = Turtle()
# """a turtle shape is provided """
# tim.shape("turtle")
# """tim color is set to blue"""
# tim.color("blue")

"""screen object is created"""
screen = Screen()
"""sets the screen setup"""
screen.setup(1000, 800)

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

# """function to create different sizes i.e from triangle to decagon"""
# def timMakePolygon(angle, color):
#     tim.color(color)
#     tim.forward(100)
#     tim.right(angle)
#
# colors = ["#ade8f4", "#90e0ef", "#48cae4", "#00b4d8", "#0096c7", "#0077b6", "#023e8a", "#03045e"]
# count = 0
# for i in range(3, 11):
#     color = colors[count]
#     for j in range(0, i):
#         timMakePolygon(360/i, color)
#     count += 1

"""create a random walk"""
# tim's configurations
# turtle.setworldcoordinates(-450, -350, 450, 350)
turtle.colormode(255)
tim.shape("turtle")
tim.speed("fastest")
tim.pensize(20)

directions = [0, 90, 180, 270]
pensizes = [10, 15, 20, 25, 20]
distances = [20, 25, 30, 35, 40]
# colors = ["#19381F", "#EEE82C", "#91CB3E", "#53A548", "#C8AB83", "#F7BFB4", "#9CBFA7",
#           "#71697A", "#BF4E30", "#FFD9DA", "#B5DFCA", "#FCFAFA", "#FFD166", "#FF47DA",
#           "#3DD6D0", "#881600", "#F08A4B", "#011936", "#F7F052", "#050401"]
def generateColor():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

for i in range(200):
    tim.color(generateColor())
    tim.setheading(random.choice(directions))
    tim.pensize(random.choice(pensizes))
    tim.forward(random.choice(distances))

tim.hideturtle()


"""screen will be exited upon a click"""
screen.exitonclick()
