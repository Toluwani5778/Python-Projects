# Python mid-term exam practice

# Minimum finding function without loop

def min ():
    num_list = []
    
    num1=int(input("Please enter a number: "))
    num_list.append(num1)
    
    num2=int(input("Please enter a number: "))
    num_list.append(num2)
    
    num3=int(input("Please enter a number: "))
    num_list.append(num3)

    if num_list[0] < num_list[1] and num_list[0] < num_list[2]:
        temp_min = num_list[0]
        
    elif num_list[1] < num_list[0] and num_list[1] < num_list[2]:
        temp_min = num_list[1]

    elif num_list[2] < num_list[1] and num_list[2] < num_list[0]:
        temp_min = num_list[2]
        
    return temp_min
        

##test = min()
##print("Lowest number:", test)
##test = min()
##print("Lowest number:", test)

# Sum of the numbers

import random

list = random.sample(range(20,99),10)

def sum(list):
    total = 0
    
    for i in list:
        total += i
        
    return total

##print(list)


##test = sum(list)
##print("Total sum is:", test)

# Printing positions

def pos(list):
    for p in range(len(list)):
        return p
        

# Printing each element on the list with position

def each (list):
    count = 0
    for i in list:
        count += 1
        print("Current number on position", count,"is:", i)


