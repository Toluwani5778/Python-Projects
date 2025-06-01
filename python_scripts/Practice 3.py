salary = float(input("Please type in your salary "))
bonus = float(input("Please type in your bonus "))
paycheck=salary+bonus
print(paycheck)
print("Your paycheck is",paycheck)
print("Your paycheck is "+ str(paycheck))
#Question why the code in # cant work below
#print("Your paycheck is "+paycheck)
#Answer: because paycheck is a number and you cant
#use the + sign to join number and string together. so you either convert
#to str or use , sign to separate them
#There are functions to convert from one datatype to another
#int(value) converts to an integer
#long(value) converts to an long integer
#float(value) converts to a floating number
    #(i.e. a number that can hold decimal places)
#str(value) converts to an integer
