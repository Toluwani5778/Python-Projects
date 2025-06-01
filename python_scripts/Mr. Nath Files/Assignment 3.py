# NAME: Amarnath
# COURSE: CS142A
# Assignment 3
# Points 20
# sorting numbers in a list
# No late submissions are accepted
# You must provide the code and the screenshot
# Your code must be annotated by the description of each question (above the cod
# Your code must be annotated by the number of point (above the code)
# Not submitting the source code will result in NO POINTS
#_________________________________________________________________________________________________________________________________________________________________

#||||||||||||||||||||||||||||||||||||||||
#                                       |
# [5 points]                            |
# voting on the ML&AI course on NUoodle |
#                                       |
#||||||||||||||||||||||||||||||||||||||||

# Answer: Successfully voted

#......................................................................
# To avoid using the underscores (line) I created a function for line .
#......................................................................


def line():
    print("_______________________________________________________________________________________________________________________________________________")


#|||||||||||||||||||||||||||||||||||||||||||||||||||||
#                                                    |
# [5 points]                                         |
# write a function that accepts a list of numbers    |
# call the function: sort_by_min_removal()           |
# sort them by removing the miminum, one at a time   |
# the results will be stored in a temporary list     |
# and return the new list                            |
#                                                    |
#|||||||||||||||||||||||||||||||||||||||||||||||||||||


def sort_by_min_removal(list_of_nums):
    new_list = []
    nums = list_of_nums
    while nums:
        minimum = nums[0]  
        for i in nums: 
            if i < minimum:
                minimum = i
        new_list.append(minimum)
        nums.remove(minimum)    

    return new_list


#|||||||||||||||||||||||||||||||||||||||||||||||||||
#                                                  |
# [8 points]                                       |
# write a function that accepts a list of numbers  |
# call the function: sort_by_swapping()            |
# sort comparing the numbers in the list           |
# the bigger is swapped with the smaller           |
# and return the exact same list                   |
#                                                  |
#|||||||||||||||||||||||||||||||||||||||||||||||||||


def sort_by_swapping(list_of_nums):
    for i in range(0, len(list_of_nums)):
        
        for j in range(i+1, len(list_of_nums)):
            if list_of_nums[j] < list_of_nums[i]:
        
                temp = list_of_nums[i]
                list_of_nums[i] = list_of_nums[j]
                list_of_nums[j] = temp
        
        # Another way to swap without creating an empty list ex: a,b = b,a
        
        # list_of_nums[i], list_of_nums[mini] = list_of_nums[mini], list_of_nums[i]
        
    return list_of_nums

    
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                                                                                  |
# [2 points]                                                                       |
# test the two function using the following lists:                                 |
# [18, -3, 0, 17, 3, -5, 14, 20, -132, 4, 0, 232]                                  |
# [730, 1992, 0, 1127, 56453, -52321231, 1131234, 21230, -112312332, 413, 0, 212]  |
# [1128, -32322, 10, 11237, 34323, -5234, 1234234, 2234230, -11232, 4, 0, 989807]  |
#                                                                                  |
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


def main():

    list_1 = [18, -3, 0, 17, 3, -5, 14, 20, -132, 4, 0, 232]
    list_2 = [730, 1992, 0, 1127, 56453, -52321231, 1131234, 21230, -112312332, 413, 0, 212]
    list_3 = [1128, -32322, 10, 11237, 34323, -5234, 1234234, 2234230, -11232, 4, 0, 989807]
    
    line()

    print()          
    print("List 1 =", list_1)
    print()
    print("List 2 =", list_2)
    print()
    print("List 3 =", list_3)
    print()

    rem_test_1 = sort_by_min_removal(list_1)
    rem_test_2 = sort_by_min_removal(list_2)
    rem_test_3 = sort_by_min_removal(list_3)

    line()

    print()        
    print("Sorted list 1 using 'sort_by_min_removal' :", rem_test_1)
    print()          
    print("Sorted list 2 using 'sort_by_min_removal' :", rem_test_2)
    print()          
    print("Sorted list 3 using 'sort_by_min_removal' :", rem_test_3)
    print()
    
    list_1 = [18, -3, 0, 17, 3, -5, 14, 20, -132, 4, 0, 232]
    list_2 = [730, 1992, 0, 1127, 56453, -52321231, 1131234, 21230, -112312332, 413, 0, 212]
    list_3 = [1128, -32322, 10, 11237, 34323, -5234, 1234234, 2234230, -11232, 4, 0, 989807]
    
    swap_test_1 = sort_by_swapping(list_1)
    swap_test_2 = sort_by_swapping(list_2)
    swap_test_3 = sort_by_swapping(list_3)


    line()

    print()          
    print("Sorted list 1 using 'sort_by_swapping' :", swap_test_1)
    print()
    print("Sorted list 2 using 'sort_by_swapping' :", swap_test_2)
    print()
    print("Sorted list 3 using 'sort_by_swapping' :", swap_test_3)
    print()
              
    line()
    
main()

