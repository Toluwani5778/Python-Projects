# class Toluwani():
#     def add(a,b):
#         print(a+b)
# class Olukanni(Toluwani):
#     pass
# a= Olukanni.add(2,5)
# print(a)

# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def salary(self,hours,rate):
#         self.hours=hours
#         self.rate=rate
#         return(self.hours)*(self.rate)
#
# Jc= Employee("John",21)
# pay=Jc.salary(15,12)
# print(pay)
# print(Jc.name)
# print(Jc.age)
# Brian=Employee("Brian",22)
# print(Brian.name)
# print(Brian.age)

# print(Toluwani)

# class Employee:
#     University="Norwich"
#     def __init__(self,name,age,ID):
#         self.name=name
#         self.age=age
#         self.ID=ID
#     def payCheck(self,hours,wage):
#         self.hours=hours
#         self.wage=wage
#         if hours>40:
#             salary=40*wage+(hours-40)*2*wage
#             return salary
#         else:
#             salary=hours*wage
#             return salary
#
# Emp_1=Employee("Toluwani",17,"A01048499")
# Check=Emp_1.payCheck(22,15)
# Emp_2=Employee("Majd",18,"A01059762")
# Check2=Emp_2.payCheck(19,15)
#
# print(f"""The First Employee data is:
#  Name: {Emp_1.name}
#  Age: {Emp_1.age}
#  University: {Emp_1.University}
#  Id: {Emp_1.ID}
#  Paycheck: ${Check}""")
# print(f"""The Second Employee data is:
#  Name: {Emp_2.name}
#  Age: {Emp_2.age}
#  University: {Emp_2.University}
#  Id: {Emp_2.ID}
#  Paycheck: ${Check2}""")

# def oper(a,b,c):
#     x=a+b+c
#     y=a-b-c
#     z=a*b*c
#     w=a-b*b
#     return w,x,y,z
# w,x,y,z=oper(2,4,6,)
# print

#Quiz
# class Vehicle:
#     def __init__(self,max_speed,mileage):
#         self.max_speed=max_speed
#         self.mileage=mileage
# BMW=Vehicle(220,17)
# print(BMW.max_speed)
# print(BMW.mileage)
#
# class Bus(Vehicle):
#     pass
#
# class University:
#     pass

# class traqazoid():
#     def __init__(self,a,b,c,d,h):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#         self.h=h
#     def area(self):
#         return 0.5*self.h*(self.a+self.b)
#     def per(self):
#         return self.a+self.b+self.c+self.d
# Rami=traqazoid(1,2,3,4,2)
# Rami.area
# import math
#
# Celsius=[0,24,56,78,100]
# Fahrenheit=[(x*1.8)+32 for x in Celsius]
# print(Fahrenheit)
#

x=[1,2,3]
y=[4,3,5]
z=[s+b for (s,b) in zip(x,y)]
print(z)

# import math
# list1=[5,6,7,8,9]
# list2=[2,4,3,6,6]
# list4=[math.sqrt((a**2) + (b**2)) for (a,b) in zip(list1,list2)]
# print(list4)

# def fun (a,b,c): #function version
#     return a*b-c
# print(fun(5,6,7))
# A=lambda a,b,c: a*b-c #Lambda version
# print(A(5,6,7))

# def fun(x):
#     return x+2
# list1=[1,3,5]
# list2=[fun(x) for x in list1] #list comprehension method
# print(list2)
#
# list3=[]
# for x in list1: #loop method
#     list3.append(fun(x))
# print(list3)
#
# list4=list(map(fun,list1)) #map method
# print(list4)

# x=[1,2,3]
# y=[4,5,6]
# z=[]
# for c in range(len(x)):
#     z.append(x[c]+y[c])
# print(z)

# x=[1,2,3]
# y="abc"
#
# z1=list(zip(x,y))
# print(z1)

num=[1,2,3,4]
A=lambda num: num*3
    print(A())