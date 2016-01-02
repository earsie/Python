#This Python file assumes there are three branches for a business--in Portland, Or; New York, NY; and London, UK--and uses Python's
#datetime module to see if they are open at present.  Pytz could have been used, but this is a way of using code to avoid Pytz.

import datetime

#Establish the local time based on user's system.  And adjust for time diffs.

PortlandTime = datetime.datetime.now()
NewYorkAdj = datetime.timedelta(hours=3)
LondonAdj = datetime.timedelta(hours=8)

NewYorkTime = PortlandTime + NewYorkAdj
LondonTime = PortlandTime + LondonAdj

#Convert time datatype to integer to perform math

pdxHour = getattr(PortlandTime, 'hour')
nyHour = getattr(NewYorkTime, 'hour')
londHour = getattr(LondonTime, 'hour')

#Test to see if integer math works

print pdxHour
print nyHour
print londHour

#Set parameters for open vs. closed in terms of hours. 
    
if (9 < pdxHour < 21):
    print("The Portland branch is still open")
else:
    print("The Portland branch is now closed")

if (9 < nyHour < 21):
    print("The New York branch is still open")
else:
    print("The New York branch is now closed")

if (9 < londHour < 21):
    print("The London branch is still open")
else:
    print("The London branch is now closed")


