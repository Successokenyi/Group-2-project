import datetime 
from playsound import playsound
alarmHour = int(input("Enter hour :  "))
alarmMin = int(input("Enter Minutes :  "))
alarmAm = input("am \ pm: " )

if alarmAm == "pm":
    alarmHour +=12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing..")
        playsound("ring2-mp3-6551.mp3")
        break 
