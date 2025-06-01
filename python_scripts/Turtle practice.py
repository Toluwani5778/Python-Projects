# #Sasuke Mangekyou Sharingan
# import turtle as t
#
# #eye circle
# t.title("Sasuke Mangekyou Sharingan")
# t.bgcolor('#bf0404')
# t.pensize(10)
# t.speed(5)
# t.color('black')
# t.pu()
# t.goto(0,200)
# t.pd()
# t.fillcolor('black')
# t.begin_fill()
# t.circle(-200)
# t.end_fill()
#
# # internal red eyes
# t.color('black')
# t.pu()
# t.goto(0,190)
# t.pd()
# t.seth(-60)
# t.fillcolor('red')
# t.begin_fill()
# t.circle(-380,60)
# t.rt(120)
# t.circle(-380,60)
# t.end_fill()
#
# t.pu()
# t.goto(-164.5,95)
# t.pu
# t.seth(0)
# t.fillcolor('red')
# t.begin_fill()
# t.circle(-380,60)
# t.rt(120)
# t.circle(-380,60)
# t.end_fill()
#
# t.color('black')
# t.pu()
# t.goto(170.5,100)
# t.pu
# t.seth(-118)
# t.fillcolor('red')
# t.begin_fill()
# t.circle(-380,60)
# t.rt(120)
# t.circle(-380,60)
# t.end_fill()
#
# # internal Red eyes black borders
# t.color('black')
# t.pu()
# t.goto(0,190)
# t.pd()
# t.seth(-60)
# t.circle(-380,60)
# t.rt(120)
# t.circle(-380,60)
#
# t.color('black')
# t.goto(-164.5,95)
# t.seth(0)
# t.circle(-380,60)
# t.rt(120)
# t.circle(-380,60)
# t.end_fill()
# t.penup()
#
# t.goto(170.5,100)
# t.seth(-118)
# t.pendown()
# t.circle(-380,60)
# t.rt(120)
# t.circle(-380,60)
# t.end_fill()
# t.penup()
#
# #last internal eye circle
# t.goto(5.0,-14.0)
# t.pendown()
# t.fillcolor('black')
# t.begin_fill()
# t.circle(13)
# t.end_fill()
#
# t.done()
#
#
# #Three Tomoe Sharingan
# from turtle import *
# import turtle
#
# t = turtle.Turtle()
#
#
# def draw_circle(color, radius, x, y):
#     t.penup()
#     t.fillcolor(color, )
#     t.goto(x, y)
#     t.pendown()
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()
#
#
# t = turtle.Turtle()
# t.color('red', 'blue')
#
#
# def eye():
#     draw_circle("Black", 210, -22, -150)
#     draw_circle("Red", 196, -20, -135)
#     draw_circle("Black", 50, -20, 15)
#
#     t.color('Black', 'blue')
#
#     draw_circle("Black", 35, -120, -67)
#     t.color('red', 'blue')
#     draw_circle("Red", 35, -130, -65)
#     t.color('Black', 'blue')
#     draw_circle("Black", 34, -120, -60)
#
#     draw_circle("Black", 35, 98, -2)
#     t.color('red', 'blue')
#     draw_circle("Red", 35, 85, 0)
#     t.color('Black', 'blue')
#     draw_circle("Black", 34, 100, -10)
#
#     draw_circle("Black", 35, -40, 155)
#     t.color('red', 'blue')
#     draw_circle("Red", 35, -55, 150)
#     t.color('Black', 'blue')
#     draw_circle("Black", 34, -37, 148)
#     turtle.hideturtle()
#
#
# if __name__ == '__main__':
#     screensize(8000, 6000, "#f0f0f0")
#     turtle.Screen().bgcolor("#dceaf6")
#
#     pensize(3)
#     speed(9)
#     eye()
# done()
#
# #Iron Man Helmet
# import turtle
#
# rachit1 = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),
#            (-40, -20), (0, -20)],
#           [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
#            (40, 120), (0, 120)]]
# rachit2 = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),
#            (-80, -230), (-64, -210), (0, -210)],
#           [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
#            (100, -46), (50, -40), (40, -30), (0, -30)]]
# rachit3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
#            (0, -250)],
#           [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),
#            (0, -220)]]
#
# turtle.hideturtle()
# turtle.bgcolor('#000000')  # Black
# turtle.setup(500, 600)
# turtle.title("I AM IRONMAN")
# rachit1Goto = (0, 120)
# rachit2Goto = (0, -30)
# rachit3Goto = (0, -220)
# turtle.speed(2)
#
#
# def logo(a, b):
#     turtle.penup()
#     turtle.goto(b)
#     turtle.pendown()
#     turtle.color('#fc0303')  # Red
#     turtle.begin_fill()
#
#     for i in range(len(a[0])):
#         x, y = a[0][i]
#         turtle.goto(x, y)
#
#     for i in range(len(a[1])):
#         x, y = a[1][i]
#         turtle.goto(x, y)
#     turtle.end_fill()
#
#
# logo(rachit1, rachit1Goto)
# logo(rachit2, rachit2Goto)
# logo(rachit3, rachit3Goto)
# turtle.hideturtle()
# turtle.done()
#
# #Superman's Logo
# import turtle #import the required package to draw the logo
#
# t=turtle.Turtle() #set the variable ‘t’ to the function turtle.Turtle() to shorten the code throughout
# turtle.Screen().bgcolor('#0060AA') #set the color of the screen to #0060AA(Medium Persian Blue) to match Superman’s costume
#
# def curve(value): #create a function to generate curves in turtle
#     for i in range(value): #for loop to repeat the inputted value number of times
#         t.right(1) #step by step curve
#         t.forward(1)
#
# t.penup() #pen is in the up position so it will not draw
# t.setposition(0,43) #move the pen to these x and y coordinates
# t.pendown() #pen is in the down position so it will draw
# t.begin_fill() #start filling in the shape
# t.pencolor('black') #change the pen color to black
# t.fillcolor('#d40202') #change the shape fill color to #d40202(Medium Red) to match the Superman logo
# t.pensize(3) #use a pen size of 3 to create a black border
# t.forward(81.5) #the pen will move forward this number to start the shield of the logo
# t.right(49.4) #rotate the pen right 49.4 degrees
# t.forward(58) #move the pen forward by 58
# t.right(81.42) #rotate right by 81.42 degrees
# t.forward(182) #move the pen forward by 182
# t.right(98.36) #rotate the pen right by 98.36 degrees
# t.forward(182) #move the pen forward by 182
# t.right(81.42) #rotate the pen by 81.42 degrees to the right
# t.forward(58) #move the pen forward 58
# t.right(49.4) #rotate the pen to the right by 49.4
# t.forward(81.5) #move the pen forward by 81.5 to meet the start at the top of the shield
# t.end_fill() #complete the fill of the shield so the shape is closed off
# t.penup() #pen will not draw
#
# t.setposition(38,32) #now to create the yellow parts of the Superman logo
# t.pendown() #the pen is now poised to draw
# t.begin_fill() #start a new shape
# t.fillcolor('gold') #change the fill color to gold to match the Superman logo
# t.forward(13) #move the pen forward by 13
# t.right(120) #rotate the pen right by 120 degrees
# t.forward(13) #move the pen forward by 13
# t.right(120) #rotate the pen right by 120 degrees
# t.forward(13) #move the pen forward by 13
# t.end_fill() #the small triangle on the right is now complete
# t.penup() #stop the pen from drawing
#
# t.setposition(81.5,25) #now to create the larger yellow part of the Superman logo, change the position of the pen
# t.pendown() #the pen will now draw again
# t.begin_fill() #the fill is still the same color set before
# t.right(210) #rotate the pen right by 210 degrees
# t.forward(25) #move the pen forward by 25
# t.right(90) #rotate the pen right by 90 degrees
# t.forward(38) #move the pen forward by 38
# t.right(45) #rotate the pen right by 45 degrees
# t.circle(82,90) #this function is used to draw a circle in turtle, the first integer is the radius and the second is the number of degrees of the circle drawn
# t.left(90) #rotate the pen left by 90 degrees
# t.circle(82,60) #create a circle of radius 82 and only complete 60 degrees of the circle
# curve(61) #call the curve function that was previously defined, pass an integer value equal to the length of the curve desired
# t.left(90) #rotate the pen left by 90 degrees
# t.forward(57) #move the pen forward by 57
# t.left(90) #rotate the pen left by 90 degrees
# t.forward(32) #move the pen forward by 32
# t.end_fill() #fill in the larger yellow part of the logo
# t.penup() #stop drawing
# t.home() #reset the pen location to the origin so the orientation is also reset
#
# t.setposition(-69,-38) #finish the major parts of the S superimposition on the shield
# t.pendown()
# t.begin_fill()
# curve(20)
# t.forward(33)
# t.left(10)
# t.circle(82,20)
# curve(30)
# t.forward(10)
# t.right(110)
# curve(40)
# t.right(10)
# t.circle(50,10)
# curve(45)
# t.right(5)
# t.forward(45)
# t.end_fill()
# t.penup()
# t.home()
#
# t.setposition(20,-100)
# t.pendown()
# t.begin_fill()
# t.right(135)
# t.forward(27)
# t.right(90)
# t.forward(27)
# t.right(135)
# t.forward(38.18)
# t.end_fill()
# t.penup()
# t.home()
#
# t.setposition(-57,32)
# t.pendown()
# t.begin_fill()
# t.right(180)
# t.forward(18)
# t.left(45)
# t.forward(44)
# t.left(80)
# t.forward(15)
# t.left(130)
# curve(40)
# t.forward(20)
# t.end_fill()
#
# t.hideturtle() #use this command to hide the turtle so it is not visible in the final image
# turtle.exitonclick() #this command will leave the window open until it is clicked
#
# #@rachit_zone
#
# Pikachu
# import turtle
#
#
# def gajurel(x, y):
#     turtle.setx(x)
#     turtle.sety(y)
#     print(x, y)
#
#
# class Pikachu:
#
#     def __init__(self):
#         self.t = turtle.Turtle()
#         t = self.t
#         t.pensize(3)
#         t.speed(9)
#         t.ondrag(gajurel)
#
#     def meme(self, x, y):
#         self.t.penup()
#         self.t.goto(x, y)
#         self.t.pendown()
#
#     def aankha1(self, x, y):
#         self.meme(x, y)
#         t = self.t
#         t.seth(0)
#         t.fillcolor('#333333')
#         t.begin_fill()
#         t.circle(22)
#         t.end_fill()
#
#         self.meme(x, y + 10)
#         t.fillcolor('#000000')
#         t.begin_fill()
#         t.circle(10)
#         t.end_fill()
#
#         self.meme(x + 6, y + 22)
#         t.fillcolor('#ffffff')
#         t.begin_fill()
#         t.circle(10)
#         t.end_fill()
#
#     def aankha2(self, x, y):
#         self.meme(x, y)
#         t = self.t
#         t.seth(0)
#         t.fillcolor('#333333')
#         t.begin_fill()
#         t.circle(22)
#         t.end_fill()
#
#         self.meme(x, y + 10)
#         t.fillcolor('#000000')
#         t.begin_fill()
#         t.circle(10)
#         t.end_fill()
#
#         self.meme(x - 6, y + 22)
#         t.fillcolor('#ffffff')
#         t.begin_fill()
#         t.circle(10)
#         t.end_fill()
#
#     def mukh(self, x, y):
#         self.meme(x, y)
#         t = self.t
#
#         t.fillcolor('#88141D')
#         t.begin_fill()
#         #
#         l1 = []
#         l2 = []
#         t.seth(190)
#         a = 0.7
#         for i in range(28):
#             a += 0.1
#             t.right(3)
#             t.fd(a)
#             l1.append(t.position())
#
#         self.meme(x, y)
#
#         t.seth(10)
#         a = 0.7
#         for i in range(28):
#             a += 0.1
#             t.left(3)
#             t.fd(a)
#             l2.append(t.position())
#
#         #
#
#         t.seth(10)
#         t.circle(50, 15)
#         t.left(180)
#         t.circle(-50, 15)
#
#         t.circle(-50, 40)
#         t.seth(233)
#         t.circle(-50, 55)
#         t.left(180)
#         t.circle(50, 12.1)
#         t.end_fill()
#
#         #
#         self.meme(17, 54)
#         t.fillcolor('#DD716F')
#         t.begin_fill()
#         t.seth(145)
#         t.circle(40, 86)
#         t.penup()
#         for pos in reversed(l1[:20]):
#             t.goto(pos[0], pos[1] + 1.5)
#         for pos in l2[:20]:
#             t.goto(pos[0], pos[1] + 1.5)
#         t.pendown()
#         t.end_fill()
#
#         #
#         self.meme(-17, 94)
#         t.seth(8)
#         t.fd(4)
#         t.back(8)
#
#     #
#     def gaala1(self, x, y):
#         turtle.tracer(False)
#         t = self.t
#         self.meme(x, y)
#         t.seth(300)
#         t.fillcolor('#DD4D28')
#         t.begin_fill()
#         a = 2.3
#         for i in range(120):
#             if 0 <= i < 30 or 60 <= i < 90:
#                 a -= 0.05
#                 t.lt(3)
#                 t.fd(a)
#             else:
#                 a += 0.05
#                 t.lt(3)
#                 t.fd(a)
#         t.end_fill()
#         turtle.tracer(True)
#
#     def gaala2(self, x, y):
#         t = self.t
#         turtle.tracer(False)
#         self.meme(x, y)
#         t.seth(60)
#         t.fillcolor('#DD4D28')
#         t.begin_fill()
#         a = 2.3
#         for i in range(120):
#             if 0 <= i < 30 or 60 <= i < 90:
#                 a -= 0.05
#                 t.lt(3)
#                 t.fd(a)
#             else:
#                 a += 0.05
#                 t.lt(3)
#                 t.fd(a)
#         t.end_fill()
#         turtle.tracer(True)
#
#     def kaan1(self, x, y):
#         t = self.t
#         self.meme(x, y)
#         t.fillcolor('#000000')
#         t.begin_fill()
#         t.seth(330)
#         t.circle(100, 35)
#         t.seth(219)
#         t.circle(-300, 19)
#         t.seth(110)
#         t.circle(-30, 50)
#         t.circle(-300, 10)
#         t.end_fill()
#
#     def kaan2(self, x, y):
#         t = self.t
#         self.meme(x, y)
#         t.fillcolor('#000000')
#         t.begin_fill()
#         t.seth(300)
#         t.circle(-100, 30)
#         t.seth(35)
#         t.circle(300, 15)
#         t.circle(30, 50)
#         t.seth(190)
#         t.circle(300, 17)
#         t.end_fill()
#
#     def jiu(self):
#         t = self.t
#
#         t.fillcolor('#F6D02F')
#         t.begin_fill()
#         #
#         t.penup()
#         t.circle(130, 40)
#         t.pendown()
#         t.circle(100, 105)
#         t.left(180)
#         t.circle(-100, 5)
#
#         #
#         t.seth(20)
#         t.circle(300, 30)
#         t.circle(30, 50)
#         t.seth(190)
#         t.circle(300, 36)
#
#         #
#         t.seth(150)
#         t.circle(150, 70)
#
#         #
#         t.seth(200)
#         t.circle(300, 40)
#         t.circle(30, 50)
#         t.seth(20)
#         t.circle(300, 35)
#         # print(t.pos())
#
#         #
#         t.seth(240)
#         t.circle(105, 95)
#         t.left(180)
#         t.circle(-105, 5)
#
#         #
#         t.seth(210)
#         t.circle(500, 18)
#         t.seth(200)
#         t.fd(10)
#         t.seth(280)
#         t.fd(7)
#         t.seth(210)
#         t.fd(10)
#         t.seth(300)
#         t.circle(10, 80)
#         t.seth(220)
#         t.fd(10)
#         t.seth(300)
#         t.circle(10, 80)
#         t.seth(240)
#         t.fd(12)
#         t.seth(0)
#         t.fd(13)
#         t.seth(240)
#         t.circle(10, 70)
#         t.seth(10)
#         t.circle(10, 70)
#         t.seth(10)
#         t.circle(300, 18)
#
#         t.seth(75)
#         t.circle(500, 8)
#         t.left(180)
#         t.circle(-500, 15)
#         t.seth(250)
#         t.circle(100, 65)
#
#         #
#         t.seth(320)
#         t.circle(100, 5)
#         t.left(180)
#         t.circle(-100, 5)
#         t.seth(220)
#         t.circle(200, 20)
#         t.circle(20, 70)
#
#         t.seth(60)
#         t.circle(-100, 20)
#         t.left(180)
#         t.circle(100, 20)
#         t.seth(300)
#         t.circle(10, 70)
#
#         t.seth(60)
#         t.circle(-100, 20)
#         t.left(180)
#         t.circle(100, 20)
#         t.seth(10)
#         t.circle(100, 60)
#
#         #
#         t.seth(180)
#         t.circle(-100, 10)
#         t.left(180)
#         t.circle(100, 10)
#         t.seth(5)
#         t.circle(100, 10)
#         t.circle(-100, 40)
#         t.circle(100, 35)
#         t.left(180)
#         t.circle(-100, 10)
#
#         #
#         t.seth(290)
#         t.circle(100, 55)
#         t.circle(10, 50)
#
#         t.seth(120)
#         t.circle(100, 20)
#         t.left(180)
#         t.circle(-100, 20)
#
#         t.seth(0)
#         t.circle(10, 50)
#
#         t.seth(110)
#         t.circle(100, 20)
#         t.left(180)
#         t.circle(-100, 20)
#
#         t.seth(30)
#         t.circle(20, 50)
#
#         t.seth(100)
#         t.circle(100, 40)
#
#         #
#         t.seth(200)
#         t.circle(-100, 5)
#         t.left(180)
#         t.circle(100, 5)
#         t.left(30)
#         t.circle(100, 75)
#         t.right(15)
#         t.circle(-300, 21)
#         t.left(180)
#         t.circle(300, 3)
#
#         #
#         t.seth(43)
#         t.circle(200, 60)
#
#         t.right(10)
#         t.fd(10)
#
#         t.circle(5, 160)
#         t.seth(90)
#         t.circle(5, 160)
#         t.seth(90)
#
#         t.fd(10)
#         t.seth(90)
#         t.circle(5, 180)
#         t.fd(10)
#
#         t.left(180)
#         t.left(20)
#         t.fd(10)
#         t.circle(5, 170)
#         t.fd(10)
#         t.seth(240)
#         t.circle(50, 30)
#
#         t.end_fill()
#         self.meme(130, 125)
#         t.seth(-20)
#         t.fd(5)
#         t.circle(-5, 160)
#         t.fd(5)
#
#         #
#         self.meme(166, 130)
#         t.seth(-90)
#         t.fd(3)
#         t.circle(-4, 180)
#         t.fd(3)
#         t.seth(-90)
#         t.fd(3)
#         t.circle(-4, 180)
#         t.fd(3)
#
#         #
#         self.meme(168, 134)
#         t.fillcolor('#F6D02F')
#         t.begin_fill()
#         t.seth(40)
#         t.fd(200)
#         t.seth(-80)
#         t.fd(150)
#         t.seth(210)
#         t.fd(150)
#         t.left(90)
#         t.fd(100)
#         t.right(95)
#         t.fd(100)
#         t.left(110)
#         t.fd(70)
#         t.right(110)
#         t.fd(80)
#         t.left(110)
#         t.fd(30)
#         t.right(110)
#         t.fd(32)
#
#         t.right(106)
#         t.circle(100, 25)
#         t.right(15)
#         t.circle(-300, 2)
#         ##############
#         # print(t.pos())
#         t.seth(30)
#         t.fd(40)
#         t.left(100)
#         t.fd(70)
#         t.right(100)
#         t.fd(80)
#         t.left(100)
#         t.fd(46)
#         t.seth(66)
#         t.circle(200, 38)
#         t.right(10)
#         t.fd(10)
#         t.end_fill()
#
#         #
#         t.fillcolor('#923E24')
#         self.meme(126.82, -156.84)
#         t.begin_fill()
#
#         t.seth(30)
#         t.fd(40)
#         t.left(100)
#         t.fd(40)
#         t.pencolor('#923e24')
#         t.seth(-30)
#         t.fd(30)
#         t.left(140)
#         t.fd(20)
#         t.right(150)
#         t.fd(20)
#         t.left(150)
#         t.fd(20)
#         t.right(150)
#         t.fd(20)
#         t.left(130)
#         t.fd(18)
#         t.pencolor('#000000')
#         t.seth(-45)
#         t.fd(67)
#         t.right(110)
#         t.fd(80)
#         t.left(110)
#         t.fd(30)
#         t.right(110)
#         t.fd(32)
#         t.right(106)
#         t.circle(100, 25)
#         t.right(15)
#         t.circle(-300, 2)
#         t.end_fill()
#
#         self.topi(-134.07, 147.81)
#         self.mukh(-5, 25)
#         self.gaala1(-126, 32)
#         self.gaala2(107, 63)
#         self.kaan1(-250, 100)
#         self.kaan2(140, 270)
#         self.aankha1(-85, 90)
#         self.aankha2(50, 110)
#         t.hideturtle()
#
#     def topi(self, x, y):
#         self.meme(x, y)
#         t = self.t
#         t.fillcolor('#CD0000')
#         t.begin_fill()
#         t.seth(200)
#         t.circle(400, 7)
#         t.left(180)
#         t.circle(-400, 30)
#         t.circle(30, 60)
#         t.fd(50)
#         t.circle(30, 45)
#         t.fd(60)
#         t.left(5)
#         t.circle(30, 70)
#         t.right(20)
#         t.circle(200, 70)
#         t.circle(30, 60)
#         t.fd(70)
#         # print(t.pos())
#         t.right(35)
#         t.fd(50)
#         t.circle(8, 100)
#         t.end_fill()
#         self.meme(-168.47, 185.52)
#         t.seth(36)
#         t.circle(-270, 54)
#         t.left(180)
#         t.circle(270, 27)
#         t.circle(-80, 98)
#
#         t.fillcolor('#444444')
#         t.begin_fill()
#         t.left(180)
#         t.circle(80, 197)
#         t.left(58)
#         t.circle(200, 45)
#         t.end_fill()
#
#         self.meme(-58, 270)
#         t.pencolor('#228B22')
#         t.dot(35)
#
#         self.meme(-30, 280)
#         t.fillcolor('#228B22')
#         t.begin_fill()
#         t.seth(100)
#         t.circle(30, 180)
#         t.seth(190)
#         t.fd(15)
#         t.seth(100)
#         t.circle(-45, 180)
#         t.right(90)
#         t.fd(15)
#         t.end_fill()
#         t.pencolor('#000000')
#
#     def start(self):
#         self.jiu()
#
#
# def main():
#     print('Painting the Cartoon... ')
#     turtle.screensize(800, 600)
#     turtle.title('Pikachu')
#     pikachu = Pikachu()
#     pikachu.start()
#     turtle.mainloop()
#
#
# if __name__ == '__main__':
#     main()