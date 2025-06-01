import sys
f=float(input("First number: "))
s=float(input("Second number: "))
try:
    e=f/s
    print(f"The answer is {e}")
except:
    error=sys.exc_info()
    print(error)