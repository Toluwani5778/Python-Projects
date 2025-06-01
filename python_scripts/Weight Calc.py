L=float(input("Please input your weight value i.e only the digits: "))
Unit=input("Specify the unit (pounds or kilograms): ")
if Unit.lower()=="pounds" or "lb":
    W=0.454*L
    print("Your weight is", L, "pounds or", W, "kilograms")
elif Unit.lower()=="kilograms" or "kg":
    g=2.205*L
    print("Your weight is", g, "pounds or", L, "kilograms")
else:
    print("Error, Please try again and follow instructions carefully")