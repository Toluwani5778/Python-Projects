
# A=[[8,14,-6],[12,7,4],[-11,3,21]]
#
# B=[[3, 16, -6], [9,7,-4],[-1,3,13]]
#
# result= [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(A)):
#  for j in range(len(B[0])):
#     for k in range(len(B)):
#         result[i][j]+=A[i][k]*B[i][j]
#
# print(result)
#
# import numpy as np
# A=np.array([[1,2], [4,5]])
# B=np.array([[1,2], [4,5]])
# result=A.dot(B)
#
# print(result)
#
# a='This is the beginning of the end of the world. Toluwani has a lot of money'
#
# c=['Majd','ahmad','rami','Saeeed','Loay']
# username = input("Put you name to choose a username: ")
# final_username = username.replace("Majd", "majdkh09")
# if final_username == 'majdkh09':
#     print("Your username is: " + final_username)
# else:
#     print('This not the owner')
#
# import numpy as np
# import matplotlib.pyplot as plt
# x=np.arange(1,6,0.1)
# y1=np.sin(x)
# y2=np.cos(x)
# plt.plot(x,y1, label='sin')
# plt.plot(x,y2, linestyle="solid", label="cos")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("sin and cos")
# plt.grid()
# plt.show()

# my_dict={''}
# A={'car':'BMW',
#    "model":"i8",
#    "color":"Black"}
# for i in A:
#     print(A[i])

#my_dict={1:5,2:7}
#
#
# for i in my_dict:
#     c==sum(my_dict.keys)
#     c==sum(my_dict.values)
#     print(c)
#
# dict={}
# for i in range(1,16):
#     dict[i]=i*2
# print(dict)
# total=0
# x=0
# while x<11:
#     total +=x
#     x=x+1
#     print(total)

# total=0
# for i in range(1,1001,1):
#     total+=i
#     print(total)
# sum=0
# for x in range(2,1001,2):
#     sum=sum+x
#     print(sum)
# A=[[1,2,4],[4,5,6]]
# print(len(A))  #number of rows
# print(len(A[0]))  #numer of columns
# print(A[0][1])
#
# for i in range(len(A)):
#     for J in range(len(A[0])):
#         print(A[i][J]+2)
#
# results=[[0,0,0],[0,0,0]]
# A=[[1,2,3],[2,3,4]]
# B=[[4,5,6],[2,3,4]]
# for i in range (len(A)):
#     for j in range(len(A[0])):
#         print(B[i][j]==[i*2])
# A=True
# print(type(A))
# odd=[1,9]
# odd.insert(7,5)
# print(odd)
# odd[2:2]=[5,3]
# print(odd)
# del (odd[1])
# print(odd)
