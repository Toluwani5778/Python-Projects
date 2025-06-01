import datetime
currentDate=datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)
print(currentDate.strftime("%d %B, %Y"))
print(currentDate.strftime("%d %b, %y"))
print(currentDate.strftime("Please can you attend our event on %A, %B %d in the year %Y"))

userinput=input("Please enter your birthday in this format (mm/dd/yyyy) ")
birthday=datetime.datetime.strptime(userinput, "%m/%d/%Y").date()
print(birthday)
days=birthday-currentDate
print(days)
print(days.days)
