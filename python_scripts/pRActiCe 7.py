# answer="0"
# while answer !="4":
#     answer=input("What is 2 + 2 = ")
# print("Correct")

# import turtle
# correct=0
# while correct < 4:
#     turtle.forward(100)
#     turtle.right(90)
#     correct+=1 # same as correct = correct + 1

#program to sort a list using imput
# i=int(input("Please enter the number of people attending the party: "))
# j=[]
# for c in range(i):
#     l=input("Please enter a name: ")
#     j.append(l)
# j.sort()
# print(j)

#Code to make a list from User input
# def add():
#     num=input("Please enter the elements of your list separated by: ")
#     user_list=num.split()
#     for i in range(len(user_list)):
#         user_list[i]=int(user_list[i])
#     print(f"Sum= {user_list}")
#     print("Sum =", sum(user_list))
# add()

# def my_max():
#     num=input("Please Enter the elements separated by comma: ")
#     User_list=num.split(",")
#     for i in range(len(User_list)):
#         User_list[i] = int(User_list[i])
#     maxo=max(User_list)
#     print(f"The largest Number is: {maxo}")
#
# my_max()

# import math
# a=3
# b=4
# c=math.hypot(a,b)
# print(c)
#
# def add(x,y):
#     return x+y
# print(add(3,4))
#
# my_add=lambda x,y:x+y
# print(my_add(3,4))

# def sqr(a,b):
#     return a**b
# print(sqr(3,3))

# my_sqr=lambda a, b: a**b
# print(my_sqr(3,3))
#
# def my_max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# print(my_max(-1,5))
#
# my_max=lambda x,y: x if x>y else y
# max=my_max(-1,3)
# print(max)
