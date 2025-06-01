# Python Class

if 5 < 2:
    print ("5 is bigger")

##x = float(input("gimme a nummber: "))
##
##print(type(int(x)))
##print(int(x))

##def addition (x, y):
##    z = x + y
##    return z 
##
##value = addition(2,4)
##print(value)
##print(addition(5,5))

##nums = [1,2,3,4,5]
##for i in range (5):
####    print(nums[i])
##    nums[i]
##    print(i)
    
##x = int(input("Enter a number: "))
##if x == 10:
##    print("The value of x is 10, yeah")
##elif x == 5:
##    print("The value of x is 5, yeah")
##else:
##    print("its neither 10 nore 5, sorry!")
    
##def math(a,b):
##    
##    c = a + b
##    print("\tThe total of",a, "and", b, "is", c, "\n")    
##
##    avg = c/2
##    print("\tThe average of", a, "and", b, "is", avg)
##
##math(2,2)


##def equa():
##    a = float(input("Enter a value for a: "))
##    c = input("Enter a value for b: ")
##    b = int(c)
##    z = (a*a)+ (2*a*b)
##    print("The solution is: ",z)
##    return z
##equa()

##def game():
##    ques = input("Do you wanna play game? (yes/no) ")
##    if ques == "yes":
##        x = int(input("Enter a number between 1 and 10: "))
##        
##        if x == 6:
##            print("Yeah!! you won the lottery")
##            
##        elif x == 5 or 7:
##            print("Oopsie, you missed it by a number")
##            
##        else:
##            print("You're unlucky!!")
##
##    else:
##        print("It is okay. You will be fine. ")
##
##game()

##sol = 5
##func = input("wanna play? (yes/no)")
##while func == "yes":
##    
##    guess = int(input("Enter your guess:"))
##
##    if guess == sol:
##        print("Yes, It's correct")
##        func = "no"
##        
##    elif guess < sol:
##        
##        
##    elif guess > sol:
##        print("Guess lower")
##        func = input("Wanna play again? (yes/no) ")
##
##    else:    
##        print("Please enter a valid integer number")
        
##def loh(num):
##    if num == 5:
##    elif num<5:
##    elif num>5:
##    else:
##    func == "no"

##def adding():
##    
##    numbers = [10] # string elements
##    numbers.append(9) # append 5 elements
##
##    return numbers
##
### name on the index (i) is (value)

def find_min(num):
    val = num[0]
    for i in num: # for each element in num, do the following
        #print("Current I is:", i)
       
        if i < val:
            val = i
            #print("current minimum value:", val)
    return val

##numbers = append()
##minimum = find_min(numbers)
##print("Minimum is:", minimum)

##x = 0
##y = 1
##
##print(bool(x<y))

##def odd_even(x):
##    remainder = x % 2 
##    if remainder == 1:
##        return "odd"
##    else:
##        return "even"
