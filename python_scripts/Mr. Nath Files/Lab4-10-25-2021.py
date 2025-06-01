# NAME: Amarnath
# COURSE: CS142A
# LAB 4
# Points 15
# No late submissions are accepted
# You must provide the code and the screenshot
# Your code must be annotated by the description of each question (above the cod
# Your code must be annotated by the number of point (above the code)
# Not submitting the source code will result in NO POINTS
#........................................................................................................................................................





#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                                                                        |
## [1 POINT]                                                             |
## Download the file given you named: Lab4-10-25-2021.py                 |
## run it and populate your basket with grrocery item a (leas 5 items)   | 
#                                                                        |
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

# >>> Downloaded the file and filled my basket with five items



#   accepting item data
#................................................................

def accept_item_data():
    
    ### accept input from the keyboard
    ### desc, price, quantity
    
    desc = input("Item desc: ")
    price = input("Item Price: ")
    quantity = input("Item Quantity: ")
    discount_rate = input("Discount Rate: ")
    
    ### package this input as entities (items)
    item = (desc, float(price), int(quantity), float(discount_rate))

    return item

#   To calculate price after discount
#................................................................

def price_after_discount(price, quant, d_rate):
    total_before = price * quant
    discount_value = total_before * d_rate
    total_after = total_before - discount_value
    return total_after

#   To calculate price after tax
#................................................................

def price_after_tax(total_after_discount, t_rate):
    tax_value = total_after_discount * t_rate
    total_after = total_after_discount + tax_value
    return total_after

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                                                                   |                          
## [3 POINTS]                                                       |
## write a module that can only access and extract the prices       |
## name it extract_item_price()                                     |
## it should accept your populated basket                           |
## it should return the the list of prices alone                    |
#                                                                   |
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def extract_item_price(basket):
    list_of_prices = []

    for i in basket:
        list_of_prices.append(i[1])
    
    return list_of_prices

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                                                                   |
## [3 POINTS]                                                       |
## write a module that can only access and extract the quantities   |
## name it extract_item_quantities()                                |
## it should accept your populated basket                           |
## it should return the the list of quantities alone                |
#                                                                   |
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def extract_item_quantities(basket):
    list_of_quantities = []

    for i in basket:
        list_of_quantities.append(i[2])
    
    return list_of_quantities

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                                                                   |
## [4 POINTS]                                                       |
## write a function and name is: find_max_price()                   |
## it accepts the list of prices                                    |
## it returns only the maximum price                                |
#                                                                   |
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def find_max_price(price):
    temp_max = 0
    for i in price:
        if i > temp_max:
            temp_max = i
        maximum_price = temp_max      
    return maximum_price

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                                                                   |
## [4 POINTS]                                                       |
## write a function and name is: find_min_quantity()                |
## it accepts the list of prices                                    |
## it returns only the maximum price                                |
#                                                                   |
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def find_min_quantity(quantity):
    temp_min = quantity[0]
    for i in quantity:
        if i < temp_min:
            temp_min = i
        minimum_quantity = temp_min 
    return minimum_quantity

def main():

    print("Welcome back to our Grocery Store")
    print("---------------------------------")
    
    basket = []

    print("Happy Shopping!!!")
    print("-------------------")
    print()
    
    done = "No"
    while done == "No":    
        item = accept_item_data()
        after_dis = price_after_discount(item[1], item[2], item[3])
        basket.append(item)
        print("\tadding... ", item[0])
        print()
        
        print("----------------------------")
        done = input("Done shopping? [Yes/No] ")
        print("----------------------------")

        print()

        
    print("====================================================")

    list_of_price = extract_item_price(basket)
    list_of_quantity = extract_item_quantities(basket)

    print("List of prices: ", list_of_price)
    print("List of quantities: ", list_of_quantity)

    print("====================================================")

    max_price = find_max_price(list_of_price)
    min_quantity = find_min_quantity(list_of_quantity)

    print("\n\n\nThe costly product on the basket before discount is:", max_price )
    print("-----------------------------------------------------------------")
    
    
    print("\n\n\nThe item with the lowest quantity on the basket is:", min_quantity)
    print("-----------------------------------------------------------------")    

    
main()    
    
    










