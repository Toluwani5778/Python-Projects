import random
nums = random.sample(range(-99,99), 10)
 

##print("Python Class")
##
##def f(x,y,z):
##  #a=(x, "+", y, "×", z, "=", x+y*z)
##  #b=(x, "+", y, "÷", z, "=", x+y/z)
##  #average=((a+b)/2)
##  #print(average)
##
##
##def simple_interest(p,t,r):
##    #print('The principal is', p)
##    #print('The time period is', t)
##    #print('The rate of interest is',r)
##      
##    #si = (p * t * r)/100
##      
##    #print('The Simple Interest is', si)
##    #return si
##
##     
##x = input("Enter your name :")
##print("Hello", x, "How are you?")
##def x(y):
##    #print(y + y)
##    
## Guess a number game ^-^
##
##a = int(input("enter a number: "))
##b = int(input("enter a number: "))
##x = a + b
##    
##print("added value is ", x)
##
##def guess(y):
##    #if y == 50:
##  #return "Perfect!"
##
##    #elif y > 50:
##  #return "guess lower"
##
##    #elif y < 50:
##  #return "guess higher"
##
##    else:
##  return "Enter a valid number"
##
##names = ["amar", "diwash", "mangtoya"]
##num = [1,2,3,4,5]
##
##sum = 0
##
##for numbers in num:
##    print("The old sum is ", sum)
##    
##    print("The current number is", numbers)
##    
##    sum = sum + numbers
##    print("The new sum is", sum)
##    
##    print("-------------------------------")
##
##
##for name in names:
##    print("Hello,", name, "Hope you're doing well.")
##print("-------------------------------")
##    
##
##def x(nu):
##    sum = 0
##    
##    for numbers in num:
##  print("The old sum is ", sum)
##  
##  print("The current number is", numbers)
##  
##  sum = sum + numbers
##  print("The new sum is", sum)
##  
##  print("-------------------------------")
##
##
##
##check = x(num)
##print(check)
##print(check)
##
##
##nums = random.sample(range(1,99), 10)
##  
##def find_max (nums):
##    val = nums[0]
##    for i in nums:
##  if i > val:
##      val = i
##    return val
##
##test = find_max(nums)
##print("Max:",test)

##def find_min (nums):
##  val = nums[0]
##  for i in nums:
##      if i < val:
##          val = i
##  return val

##test = find_min(nums)
##print("Min:",test)
##
##
##def sort_des(nums):
##  
##    sorted_list = []
##    
##    for i in range(len(nums)):
##      
##        temp_max = find_max(nums)
##  
##        sorted_list.append(temp_max)
##  
##        nums.remove(temp_max)
##  
##    return sorted_list
##
##test = sort_des(nums)
##print("Descending order:", test)

##nums = random.sample(range(1,99), 10)


				
##
##
## Method   Description
## 
## append() Adds an element at the end of the list
## clear()  Removes all the elements from the list
## copy()           Returns a copy of the list
## count()  Returns the number of elements with the specified value
## extend() Add the elements of a list (or any iterable), to the end of the current list
## index()  Returns the index of the first element with the specified value
## insert() Adds an element at the specified position
## pop()            Removes the element at the specified position
## remove() Removes the item with the specified value
## reverse()    Reverses the order of the list
## sort()       Sorts the list
##

##this_list = ["apple", "banana", "cherry"]
##this_list.append("orange")
##this_list.append("banana")
##this_list.remove("banana")
##print(this_list)

##this_list = ["apple", "banana", "cherry"]
##this_list.insert(1, "orange")
##print(this_list)

##
##this_list = ["apple", "banana", "cherry"]
##tropical = ["mango", "pineapple", "papaya"]
##this_list.extend(tropical)
##print(this_list)
##
##this_list = ["apple", "banana", "cherry"]
##this_list.remove("banana")
##print(this_list)
##
##this_list = ["apple", "banana", "cherry"]
##this_list.pop(-1)
##print(this_list)
##
##this_list = ["apple", "banana", "cherry"]
##this_list.pop()
##print(this_list)
##
##this_list = ["apple", "banana", "cherry"]
##del this_list[0]
##print(this_list)
##
##this_list = ["apple", "banana", "cherry"]
##for i in range(len(this_list)):
##  print(this_list[i])
##
##this_list = ["apple", "banana", "cherry"]
##i = 0
##while i < len(this_list):
##  print(this_list[i])
##  i = i + 1
##
##thislist = ["apple", "banana", "cherry"]
##[print(x) for x in thislist]
##
##fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
##
##newlist = []
##
##for x in fruits:
##  if "a" in x:
##    newlist.append(x)
##
##print(newlist)
##
##fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
##
##newlist = [x for x in fruits if "a" in x]
##
##print(newlist)
##
##fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
##
##newlist = [x for x in fruits if "a" in x]
##
##print(newlist)
##
##newlist = [x for x in range(10) if x < 5]
##
##thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
##thislist.sort()
##print(thislist)
##
##thislist = [100, 50, 65, 82, 23]
##thislist.sort()
##print(thislist)
##
##thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
##thislist.sort(reverse = True)
##print(thislist)
##
##thislist = [100, 50, 65, 82, 23]
##thislist.sort(reverse = True)
##print(thislist)
##
##
##
##nums = random.sample(range(1,99), 10)
##print("Generated random numbers are", nums)
##print()
##for pos in range(0, len(nums)):
##    print("in position", pos, "and the number is", nums[pos])
##
##    
##sol = 5
##func = "yes"
##while func == "yes":
##    
##    guess = int(input("Enter your guess:"))
##
##    if guess == sol:
##        print("Yes, It's correct")
##        func = "no"
##    elif guess < sol:
##        print("Guess higher")
##    elif guess > sol:
##        print("Guess lower")
##    else:    
##        print("Please enter a valid integer number")

##list = []
##shop = "yes"
##while shop == "yes":
##    item = input("Enter the item name:")
##    list.append(item)
##    ques = input("Do you want to continue shopping? /n Say yes or no:")
##    shop = ques
##
##
##for i in range(0, len(list)):
##    if i % 2 ==0:
##        print("Item on the cart(even) is:", shop[i])
##


def hyphen():
		print()
		print("--------------------------------------------------------------------")
		print()
def star():
		print()
		print("********************************************************************")
		print()
def line():
		print()
		print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
		print()
def equal():
		print()
		print("====================================================================")
		print()
def under():
		print()
		print("____________________________________________________________________")
		print()
		
##def chat():
##    print(".................................................")
##    print(". Welcome to Norwich University Shopping Center .")
##    print(".................................................")
##
##    ques = input("\nI'm Ash. I'm here to help you with your shopping. \nReply with a 'hi' to start shopping.\n\n")
##    if ques == "hi":
##        cart = []
##        cont = "yes"
##        while cont == "yes":
##            hyphen()
##            print()
##            item = input("Enter the name of the item you want to add to the cart: ")
##            cart.append(item)
##            cont = input("Do you want to continue shopping? (yes/no) ")
##            print()
##            if cont == "no":
##                hyphen()
##                print("Your items are successfully added to the cart")
##                print()
##        return cart
##    else:
##        print("Please reply with a 'hi' to start shopping!")
##def each(my_cart):
##    for i in my_cart:
##        print("item on your cart is:", i)
##
##def pay():
##    print("The items on the cart costs $170.\n")
##    tip = float(input("Please enter the amount you like to tip: "))
##    total = 170 + tip
##    print("The total amount you have to pay is:", total)
##    print()
##    input("Choose an option to pay (card / cash): ")
##    print()
##    print("Your transaction is successfull!")
##    print(" _______________________________")
##    print("|                               |")
##    print("|  Thanks for shopping with us  |")
##    print("|_______________________________|")
##def main():
##    
##    
##    my_cart = chat()
##    line()   
##    print()
##    each(my_cart)
##    print()
##    line()
##    print()
##    pay()
##    
##main()

# Count function

##list = random.sample(range(-99,99), 10)
##print(list)



##def finding():
##    nums = list
##    print(nums)
##    find = int(input("Enter a number you want to find: "))
##    count = nums.count(find)
##    print(count)
##finding()

##def finder(nums, n):
##    count = 0
##    for n in nums:
##        if nums == n:
##            count += 1
##    return count

##print("List of numbers:", list)
##ans = finder(list, 45)
##print("Count is:", ans)
##
#### Index function
#x = int(input("Enter a number you want to search: "))
##counting = list.count(x)
##pos = list.index(x)
##print("There are", counting, "number of", x, "in position", pos)

# writing function instead of using easy index function

##def fun(list, n):
##    for i in range (0, len(list)):
##        if list[i] == n:
##            return i
##print(fun(list, x))

##class ourlist:
##    
##    def __init__(self, n):
##        self.list = n
##
##    def our_index(self, num):
##        for i in range(0,len(self.list)):
##            if self.list[i] == num:
##                return i
##    def finder(nums, n):
##        count = 0
##        for n in nums:
##            if nums == n:
##                count += 1
##        return count
##
##list_objects = ourlist([1,2,3,4,5])
##pos = list_objects.our_index(7)
##print("Position is:", pos)



##def demo(x):
##    result =""
##    splits = x.split()
##    for i in splits:
##        print("words:", i)
####    for i in x:
####        result = result + i
####    return result
##
##word = input("Enter a word: ")
##words = demo(word)
##print(words)


##def process_text(text):
##    words = text.split()
##    comma = text.split(",")
##    dot = text.split(".")
##    
##    for word in words:
##        print("Current word ", word)
##        
##    under()
##
##    for word in comma:
##        print("Text seperated by commas:", word)
##        
##    under()
##    
##    for word in dot:
##              print("Current sentence:",dot)
##
##    under()
##    
##    for word in words:
##        
##        if word.isdigit():
##            print("Current digit is:", word)
##
##        else:
##            print("Current word is:", word)
##    under()
##    
##    for word in words:
##        if word.isupper():
##            print("The upper cased word is:", word)
##        
##        elif word.islower():
##            print("The lower cased word is:", word)
##     under()
    
##    find = input("Enter the word you want to find: ")
##    for word in words:
##        
##        if word.strip("'").strip(".").strip("!") == find:
##            print("The word '", word.strip("'").strip(".").strip("!"), "' is found!")
##            
##        else:
##            print("Oops, the word you're looking for is not here")
##
##def main():
##    text = input ("Enter the text to process: ")
##    process_text(text)
##
##main()

##
##    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
##    print("| There are", len(movie_type_set), "unique movie types in this dictionary.                                   |\n| They are:                                                                            |")
##
##    for movie_type in movie_type_set:
##        print("| \t",movie_type,"                               \t\t\t\t       |")
##    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

##movies_db={"Gabe Ibanez":["Movie","Automata",2014,110]}
##x= movie_db["Gabe Ibanez"] = ("Movie", "Automata", 2014, 110)
##print(x)
####y=movies_db["Gabe Ibanez"][1]
##print(y)

##for key in movies_db.keys():
##    print(key)
##for value in movies_db.values():
##    print(value[0])
