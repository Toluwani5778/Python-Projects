# #Turtle Race
# import turtle
# from random import *
# from turtle import *
#
# penup()
# goto(-140,140) #positioning the pen
#
# for sp in range(15): #loop for creating the lines labelled with numbers
#   speed(10)
#  #setting the speed
#   write(sp)
#  #writing the int
#   right(90)
#  #setting right at 90 degrees
#   forward(10)
#  #forward at 10 units
#   pendown()
#  #ready to draw
#   forward(150)
 #forward at 150 units
#   penup()
#  #not ready to draw
#   backward(160)
#  #back at 160 units
#   left(90)
#  #left set at 90 degrees
#   forward(20)
#  #forward at 20 units
#
#
# ankur = Turtle() #inheriting the turtle
# ankur.color('green') #setting the color to green for the first turtle
# ankur.shape('turtle') #setting the shape to "turtle"
# ankur.penup() #not ready to draw
# ankur.goto(-160,100) #positioning the turtle
# ankur.pendown() #ready todraw
#
#
# gajurel = Turtle() #inheriting another turtle
# gajurel.color('red') #setting the color og the turtle to red
# gajurel.shape('turtle') #declaring the shape of the turtle to "turtle"
# gajurel.penup() #not ready to draw
# gajurel.goto(-160,80) #positioning
# gajurel.pendown() #ready to draw
#
# turtleVar = Turtle() #inheriting the last turtle
# turtleVar.color('blue') #setting the color of the turtle as "blue"
# turtleVar.shape('turtle') #declaring the shape of the turtle
# turtleVar.penup() #not ready to draw
# turtleVar.goto(-160,60) #positioning
# turtleVar.pendown() #ready
#
# for turn in range(100): #loop for the racew
#   ankur.forward(randint(1,5)) #setting the speed randomly with the "random" module
#   gajurel.forward(randint(1,5)) #setting the speed randomly with the "random" module
#   turtleVar.forward(randint(1,5)) #setting the speed randomly with the "random" module
#
# turtle.done()

# #Batman Logo
# import turtle
# import math
#
# kalam = turtle.Turtle()
# kalam.speed(500)
#
# window = turtle.Screen()
# window.bgcolor("#000000")
# kalam.color("yellow")
#
# ankur = 20
#
# kalam.left(90)
# kalam.penup()
# kalam.goto(-7 * ankur, 0)
# kalam.pendown()
#
# for a in range(-7 * ankur, -3 * ankur, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
#                 1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
#                     4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
#                         math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
#     kalam.goto(a, y * ankur)
#
# for a in range(-3 * ankur, -1 * ankur - 1, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
#         math.fabs(rel - 1) / (rel - 1))
#     kalam.goto(a, y * ankur)
#
# kalam.goto(-1 * ankur, 3 * ankur)
# kalam.goto(int(-0.5 * ankur), int(2.2 * ankur))
# kalam.goto(int(0.5 * ankur), int(2.2 * ankur))
# kalam.goto(1 * ankur, 3 * ankur)
# print("Batman Logo with Python Turtle")
# for a in range(1 * ankur + 1, 3 * ankur + 1, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
#         math.fabs(rel - 1) / (rel - 1))
#     kalam.goto(a, y * ankur)
#
# for a in range(3 * ankur + 1, 7 * ankur + 1, 1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
#                 1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
#                     4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
#                         math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
#     kalam.goto(a, y * ankur)
#
# for a in range(7 * ankur, 4 * ankur, -1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
#     kalam.goto(a, y * ankur)
#
# for a in range(4 * ankur, -4 * ankur, -1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
#     kalam.goto(a, y * ankur)
#
# for a in range(-4 * ankur - 1, -7 * ankur - 1, -1):
#     x = a / ankur
#     rel = math.fabs(x)
#     y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
#     kalam.goto(a, y * ankur)
#
# kalam.penup()
# kalam.goto(300, 300)
# turtle.done()
