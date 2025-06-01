#Program to calculate time between two events
import datetime
Currenttime=datetime.datetime.now()
print(Currenttime)
print(Currenttime.hour)
print(Currenttime.minute)
print(Currenttime.second)
print(Currenttime.strftime("%H:%M"))
##timeinput=input("""Please enter the date you want to
##calculate for in this format (dd/mm/yyyy) """)
##Calctime=datetime.datetime.strptime(timeinput, "%d/%m/%Y").date()
##timebtw=Calctime-Todaytime
##print(timebtw)
