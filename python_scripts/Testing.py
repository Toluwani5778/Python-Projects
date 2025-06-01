#Program to calculate time until deadline
import datetime
currentDate=datetime.date.today()
userinput=input("Please enter the day of your deadline in this format (mm/dd/yyyy) ")
deadLine=datetime.datetime.strptime(userinput, "%m/%d/%Y").date()
days=deadLine-currentDate
print(days)
d=int(days.days)
print("You have",d,"days")
w=d/7
q=d%7
print("You have", int(w),"weeks and", int(q),"days")

