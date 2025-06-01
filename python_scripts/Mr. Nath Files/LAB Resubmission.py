
### function definition

def add_three_numbers (num1, num2, num3) :
 sum_of = num1 + num2 + num3
 return sum_of

### function test cases: positive, negative, with 0, repeated, all

print("TEST CASES FOR ADDING THREE NUMBERS")

sum_result = add_three_numbers(2, 4, 9)
print("Sum is: ", sum_result)

sum_result = add_three_numbers(0, 5, -2)
print("Sum is: ", sum_result)

sum_result = add_three_numbers(-2, -4, -9)
print("Sum is: ", sum_result)

sum_result = add_three_numbers(-4, -4, 8)
print("Sum is: ", sum_result)

sum_result = add_three_numbers(102, 0, -7)
print("Sum is: ", sum_result)

print("#########################################")

### function definition

def avg_three_nums (num1, num2, num3):
 sum_of_three = add_three_numbers(num1, num2, num3)
 avg_result = sum_of_three / 3
 return avg_result

### function test cases: positive, negative, with 0, repeated, all

print("TEST CASES FOR AVERAGING THREE NUMBERS")

avg_result = avg_three_nums(2, 4, 8)
print("AVG is: ", avg_result)

avg_result =avg_three_nums(0, 5, 4)
print("AVG is: ", avg_result)

avg_result =avg_three_nums(-2, -4, 6)
print("AVG is: ", avg_result)

avg_result =avg_three_nums(4, 4, -7)
print("AVG is: ", avg_result)

avg_result =avg_three_nums(102, 0, -93)
print("AVG is: ", avg_result)

#TEST CASES FOR ADDING TWO NUMBER FUNCTIONS
#Sum is: 15
#Sum is: 3
#Sum is: -15
#Sum is: 0
#Sum is: 95

#TEST CASES FOR AVERAGIGN TWO NUMBERS
#AVG is: 4.666666666666667
#AVG is: 3.0
#AVG is: 0.0
#AVG is: 0.3333333333333333
#AVG is: 3.0
