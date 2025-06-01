print("..........................................")

def simple_sum(x, y):
    sub = y + x
    return sub

sum=simple_sum(3, 0)
print("1- Adding two results:", sum)

sum=simple_sum(-5, -5)
print("2- Adding two results:", sum)

sum=simple_sum(-3, 3)
print("3- Adding two results:", sum)

print("..........................................")

def brilliant_average_four(a, b, c, d):
    num1 = simple_sum(a,b)
    num2 = simple_sum(c, d)
    add = num1 + num2
    avg = add/4
    
    return avg

avg = brilliant_average_four(2, 2, 2, 2)
print("1- Averaging four results:", avg)

avg = brilliant_average_four(-3, 4, 0, -8)
print("2- Averaging four results:", avg)

avg = brilliant_average_four(-3, 6, -2, -1)
print("3- Averaging four results:", avg)

print("..........................................")



