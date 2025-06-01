 # NAME: AMARNATH
# COURSE: CS142A
# LAB 3
# POINTS 15

# [1 point]

# Define a list of three number: 19, 12, 17 

list_numbers = [19, 12, 17]

# [.5 point]
# write the code the prints the first number 

print("My first number in the list is:", list_numbers [0])
print()

# [.5 point]
# write the code that prints the 2nd number 


print("My second number in the list is:", list_numbers [1])
print()

# [.5 point]
# write the code that prints the 3rd number 


print("My third number in the list is:", list_numbers [2])

print()
print("........................................................")
print()

# [1.5 point]
# write the code that prints the 3rd, 1st, 2nd 


print("My third number in the list is:", list_numbers [2])
print()

print("My first number in the list is:", list_numbers [0])
print()

print("My second number in the list is:", list_numbers [1])

print()
print("........................................................")
print()

# [5 point]
# define a funtion that takes a list of thee number 
# the function works on the list, not using any looping mechanism
# the function returns the minimum of three numbers: 12
list_numbers=[17, 12, 119]

def min_of_three (list_numbers):
    
    my_min = list_numbers[0]
    print("My baseline minimum setup is:", my_min)
    print()
    if list_numbers[1] < list_numbers[0]:
        my_min = list_numbers[1]
        print("My current minimum is:", my_min)
        print()
        
    elif list_numbers[2] < list_numbers[1]:
        my_min = list_numbers[2]
        print("My current minimum is:", my_min)
        print()
        
    else:
        print("My current minimum: ", list_numbers[0])
        
    return my_min

# [.5 point]
# test your code and make sure your function returrn the minimum 
# [.5 point]
# print the minimum 

print("Test one of minimum value returning function")
print("--------------------------------------------")
print()

min_val_1 = min_of_three (list_numbers)
print("Final minimum value is:", min_val_1)    
print()

# CHECKING THE MINIMUM VALUE RETURNING FUNCTION WITH DIFFERENT VALUES
# MAKING SURE MY FUNCTION IS RETURNING THE MINIMUM VALUE

print("Test two to make sure this function works with different values")
print("---------------------------------------------------------------")
print()

new_list_numbers = [2, 67, -1]
min_val_2 = min_of_three (new_list_numbers)
print("Final minimum value is:", min_val_2)

print()
print("........................................................")
print()

# [5 points]
### watch the following video:
# https://www.youtube.com/watch?v=zNxTGgTECEQ
# learn carefull the technique of adding the numbers up one step at a time
# You are asked to do the for the following --> [13, 5, 11, 7, 17, 9, ]
# I don't need code, just trace the steps in the exact same way the video is showing

list_nums = [13, 5, 11, 7, 17, 9]

def sum_elements(numbers):
    
    total_sum = 0
    for number in numbers:
        
        total_sum = total_sum + number

    return total_sum


total_after_sum = sum_elements(list_nums)
print("The total sum of numbers", list_nums[0], list_nums[1], list_nums[2], list_nums[3], list_nums[4], list_nums[5], "are: ", total_after_sum)

