# amount=float(input("Enter the amount of your total purchase "))
# if amount<50:
#     total=amount+10
#     print(f"Your final cost for purchase and shipping cost = ${total}")
# else:
#     print("Shipping is free")
#     print(f"Your final cost for purchase and shipping cost = ${amount}")
# print("Have a nice day Amigo.")
#
# amount=float(input("What is value of your total order $"))
# Country=input("Please state the Country you are from ")
# if Country.upper()=="CANADA":
#     Province=input("Please what province are you from ")
#     if Province.lower()=="alberta":
#         total=amount + (amount*0.05)
#         print(f"Your total charge for this order is ${total}")
#     elif Province.lower()=="ontario" or Province.lower()=="new brunswick" or Province.lower()=="nova scotia":
#         total=amount + (amount*0.13)
#         print(f"Your total charge for this order is ${total}")
#     else:
#         total=amount + (amount*0.06) + (amount*0.05)
#         print(f"Your total charge for this order is ${total}")
# print("Have a great day, we hope to see you again.")

# #The code below is for the shuriken turtle
# import turtle
# for x in range(5):
#     turtle.color('red')
#     turtle.forward(100)
#     turtle.right(120)
#     turtle.color('blue')
#     turtle.forward(100)
#     turtle.right(120)
#     turtle.color('green')
#     turtle.forward(100)
#     turtle.right(120)
#     turtle.right(45)
#     turtle.color('blue')
#     turtle.forward(50)
#     turtle.right(45)
#     turtle.color('yellow')
#     turtle.forward(100)

# #recurring pattern turtle
import turtle
nf = 16
for c in range(nf):
    turtle.forward(100)
    turtle.right(360 / nf)
    for v in range(nf):
        turtle.forward(50)
        turtle.right(360 / nf)

#shortcut for multiple line commenting in pycharm is ctrl + /