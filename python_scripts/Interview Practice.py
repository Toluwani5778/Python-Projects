# # The code to put user input in a list
# L1=[]
# while(1):
#     User=int(input("Please enter your numbers: "))
#     L1.append(User)
#     I=input("Do you want to continue, input 'Y' to continue or 'N' to stop input:  ")
#     if I.upper()=="Y":
#         continue
#     elif I.upper()=="N":
#         break
#     else:
#         print("The only options are 'Y' to continue or 'N' to stop")
# print(L1)
# mini=L1[0]
# for i in range(1,len(L1)):
#     if mini>L1[i]:
#         mini=L1[i]
# print(f"The minimum number is: {mini}")
#
# maxi=L1[0]
# for i in range(1,len(L1)):
#     if maxi<L1[i]:
#         maxi=L1[i]
# print(f"The maximum number is: {maxi}")
# L2=[]
# while len(L2)>0:
#     for x in L1:
#         mini = L1[0]
#         for i in range(1, len(L1)):
#             if mini > L1[i]:
#                 mini = L1[i]
#                 L2.append(mini)
#                 L1.remove(x)
#                 print(L2)

#Star triangle
# def pyfunc(r):
#     for x in range(r):
#         print(' '*(r-x-1)+'*'*(2*x+1))
# pyfunc(9)

#Palindrome code
# a=input("enter sequence")
# b=a[::-1]
# if a==b:
#   print("palindrome")
# else:
#   print("Not a Palindrome")

# Fibonacci Sequence
# a,b = 0, 1
# for i in range(0, 10):
#     print(a)
#     a, b = b, a + b

#FizzBuzz
# for num in range(1,101):
#     if num % 5==0 and num % 3 ==0:
#         print ("FizzBuzz")
#     elif num % 3 ==0:
#         print("Fizz")
#     elif num % 5 ==0:
#         print("Buzz")
#     else:
#         print(num)

#List Comprehension with Zip
# lst1= ['W', 'a', 'w','b']
# lst2 = ['e', ' ','riting','log']
# lst3 = [x + y for x, y in zip(lst1, lst2)]
# print(lst3)

# A simple generator for Fibonacci Numbers
# def fib(limit):
#     # Initialize first two Fibonacci Numbers
#     a, b = 0, 1
#
#     # One by one yield next Fibonacci Number
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
#
# # Create a generator object
# x = fib(5)
#
# # Iterating over the generator object using next
# print(next(x))  # In Python 3, __next__()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#
# # Iterating over the generator object using for
# # in loop.
# print("\nUsing for in loop")
# for i in fib(5):
#     print(i)

# with open("text.txt","r") as f:
#     print(f.read())