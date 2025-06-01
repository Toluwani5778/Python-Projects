print("1.Add")
print("2.Sub")
print("3.multiply")
print("4.divide")
u=int(input("Please type your selected operation: "))
i=float(input("What is the first number?: "))
j=float(input("What is the second number?: "))
if u==1:
    k=i+j
    print("Your answer is",k)
elif u==2:
    l=i-j
    print("Your answer is",l)
elif u==3:
    g=i*j
    print("Your answer is",g)
elif u==4:
    d=i/j
    print("Your answer is",d)
else:
    print("Error choose one of the above operations with the number")
    print("And try again")