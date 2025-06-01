# def odd_even(number):
#     if number % 2 == 0:
#         print("Your number: ", number, " is even")
#     elif number % 2 == 1:
#         print("Your number: ", number, " is odd")
#     elif number > 0:
#         print("Your number: ", number, " is positive")
#     elif number < 0:
#         print("Your number: ", number, " is negative")
#     else:
#         print("This number could be prime, fractions, anything")
#
#
# def dress_code(temp):
#     if  temp < 40:
#         print("dress warmly, it is very cold")
#     elif temp >= 40 and temp < 55:
#         print("dress warmly but not too warm")
#     elif temp >= 55 and temp < 75:
#         print("dress lightly, it is a really nice day out")
#     elif temp >= 75 and temp < 100:
#         print("Time to go to the beach ...")
#     else:
#         print("It is too hot to do anything ")


def swap_two_nums(num1, num2):
    print("num1 Before ", num1)
    print("num2 Before ", num2)    
    
    temp = num1
    num1 = num2
    num2 = temp
    
    print("num1 after", num1)
    print("num2 after", num2)
    
    
def main():
    number1 = input("Enter a number1 please: ")
    print(type(number1))
    number2 = input("Enter a number2 please: ")

    list_nums =  [number1, number2]

    swap_two_nums(list_nums[0], list_nums[1])
    
    number = input("Give me a name: ")
    print(type(number))
    
    
    
main()        