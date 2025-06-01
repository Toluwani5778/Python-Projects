a=-1
b=6
c=2
if b>5:
    c=a*c
    return c
elif b>1:
    c=c-1
    return c
else:
    b=0
a=c+b+3

while(b>1) and (a>1):
    b=b-2
    a=a-1
    return a and b
count = 4
while count>0:
    a=a+b+1
    c=c+1
    return a and c
a=a+1
b=-(1-a)
c=c-1
print("a:",a,"b:",b,"c:",c)
