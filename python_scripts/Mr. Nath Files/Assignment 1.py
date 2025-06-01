print("Welcome to Norwich Shopping center")
print("__________________________________")

print()

def item_price_after_tax (price, tax_rate):
    calc_percentage = price * tax_rate
    after_tax = calc_percentage + price

    return after_tax

def calc_total_price (price, tax_rate, quantity):
    after_tax = item_price_after_tax (price, tax_rate)
    total_cash = after_tax * quantity
    
    return total_cash


item_1 = calc_total_price (130, .05, 3)
print("The item 1 costs $130.00 and the tax rate is 0.05 and the quantity is 3 \nThe total cost of these items are:", item_1)

print()

item_2 = calc_total_price (130, .003, 5)
print("The item 2 costs $130.00 and the tax rate is 0.003 and the quantity is 5 \nThe total cost of these items are:", item_2)

print()

item_3 = calc_total_price (130, .4 , 7)
print("The item 3 costs $130.00 and the tax rate is 0.4 and the quantity is 7 \nThe total cost of these items are:", item_3)

print()

item_4 = calc_total_price (130, .17, 11)
print("The item 4 costs $130.00 and the tax rate is 0.17 and the quantity is 11 \nThe total cost of these items are:", item_4)

print()

item_5 = calc_total_price (130, .083, 9)
print("The item 5 costs $130.00 and the tax rate is 0.083 and the quantity is 9 \nThe total cost of these items are:", item_5)

############################################################################################################################################

def test_pos_neg (x):
    remainder = x % 2 
    if remainder == 1:
        squared_x = square_x (x)
        
        #Other way to print the answer is
        #print("The number you entered is", x, ",since its an even number the cubed value is", cube_ans)
        
        return squared_x
    else:
        cubed_x = cube_x (x)
        
        #Other way to print the answer is
        #print("The number you entered is", x, ",since its an odd number the squared value is", sq_ans)
        
        return cubed_x

def odd_even(x):
    remainder = x % 2 
    if remainder == 1:
        return "odd"
    else:
        return "even"

def square_x (x):
    sq_it = x * x
    return sq_it

def cube_x (x):
    cube_it = x * x * x
    return cube_it

def sq_cube(x):
    remainder = x % 2 
    if remainder == 1:
        return "squared"
    else:
        return "cubed"

print()
print(".....................................................................................")
print()

print("The test cases for squaring or cubing the given numbers")
print("_______________________________________________________")

print()

test_1 = test_pos_neg(29)
print("The number you entered is 29. Since its an odd number the squared value is", test_1)

print()

test_2 = test_pos_neg(290)
print("The number you entered is 290. Since its an even number the cubed value is", test_2)

print()

test_3 = test_pos_neg(-8)
print("The number you entered is -8. Since its an even number the cubed value is", test_3)

print()

test_4 = test_pos_neg(-3)
print("The number you entered is -3. Since its an odd number the squared value is", test_4)

print()

print(".....................................................................................")

############################################################################################################################################

print()
#Price of the first product
print("Enter your product details and I'll tell you the final price")
print("____________________________________________________________")

print()

price = float(input("Enter the price: "))
tax_rate = float(input("Enter the tax rate: "))
quantity = int(input("Enter the quantity of the products: "))
final_rate = calc_total_price(price, tax_rate, quantity)
print()
print("The price of the item is", price, "and the tax rate is", tax_rate, "and the total quantity is", quantity)
print("The final price you have to pay is", final_rate)


print()
#Price of the second product

price = float(input("Enter the price: "))
tax_rate = float(input("Enter the tax rate: "))
quantity = int(input("Enter the quantity of the products: "))
final_rate = calc_total_price(price, tax_rate, quantity)
print()
print("The price of the item is", price, "and the tax rate is", tax_rate, "and the total quantity is", quantity)
print("The final price you have to pay is", final_rate)

print()
#Price of the third product

price = float(input("Enter the price: "))
tax_rate = float(input("Enter the tax rate: "))
quantity = int(input("Enter the quantity of the products: "))
final_rate = calc_total_price(price, tax_rate, quantity)
print()
print("The price of the item is", price, "and the tax rate is", tax_rate, "and the total quantity is", quantity)
print("The final price you have to pay is", final_rate)

print()
#Price of the fourth product

price = float(input("Enter the price: "))
tax_rate = float(input("Enter the tax rate: "))
quantity = int(input("Enter the quantity of the products: "))
final_rate = calc_total_price(price, tax_rate, quantity)
print()
print("The price of the item is", price, "and the tax rate is", tax_rate, "and the total quantity is", quantity)
print("The final price you have to pay is", final_rate)

print()
#Price of the fifth product

price = float(input("Enter the price: "))
tax_rate = float(input("Enter the tax rate: "))
quantity = int(input("Enter the quantity of the products: "))
final_rate = calc_total_price(price, tax_rate, quantity)
print()
print("The price of the item is", price, "and the tax rate is", tax_rate, "and the total quantity is", quantity)
print("The final price you have to pay is", final_rate)

print()



############################################################################################################################################

print()
print("Enter a number and I will tell you whether It's even or odd and run the functions accordingly")
print("_____________________________________________________________________________________________")
print()

find_odd_even = int(input("Enter a number: "))
pos_neg = test_pos_neg (find_odd_even)
ques_odd_even = odd_even(find_odd_even)
res_sq_cube = sq_cube(find_odd_even)
print("The number you entered is",find_odd_even, "and It's an", ques_odd_even , "number. So the", res_sq_cube ,"result is", pos_neg )
    
print()

find_odd_even = int(input("Enter a number: "))
pos_neg = test_pos_neg (find_odd_even)
ques_odd_even = odd_even(find_odd_even)
res_sq_cube = sq_cube(find_odd_even)
print("The number you entered is",find_odd_even, "and It's an", ques_odd_even , "number. So the", res_sq_cube ,"result is", pos_neg )

print()

find_odd_even = int(input("Enter a number: "))
pos_neg = test_pos_neg (find_odd_even)
ques_odd_even = odd_even(find_odd_even)
res_sq_cube = sq_cube(find_odd_even)
print("The number you entered is",find_odd_even, "and It's an", ques_odd_even , "number. So the", res_sq_cube ,"result is", pos_neg )

print()

find_odd_even = int(input("Enter a number: "))
pos_neg = test_pos_neg (find_odd_even)
ques_odd_even = odd_even(find_odd_even)
res_sq_cube = sq_cube(find_odd_even)
print("The number you entered is",find_odd_even, "and It's an", ques_odd_even , "number. So the", res_sq_cube ,"result is", pos_neg )




    
