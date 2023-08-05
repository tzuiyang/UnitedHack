import datetime

#### SET WORKHOURS ####
def setWorkHours():
    setWorkHours.workStart = int(input("Work start time: "))
    setWorkHours.workEnd = int(input("Work end time: "))
    


#### Set how many breaks  ####
def setBreaks():
    setBreaks.breakAmount = int(input("Enter how many breaks you want throughout the day: "))
    




####  SET ALARM  ####
def setAlarm():
    setAlarm.alarmHour = int(input("Enter alarm hour: "))
    if(setAlarm.alarmHour < 0 or setAlarm.alarmHour > 24):
        print("Invalid time")
        return False
    setAlarm.alarmMin = int(input("Enter alarm minutes: "))
    if(setAlarm.alarmMin < 0 or setAlarm.alarmMin > 60):
        print("Invalid time")
        return False


setWorkHours()
setBreaks()
alarmHourList = []
alarmMinList = []

for i in range(setBreaks.breakAmount):
    setAlarm()
    alarmHourList.append(setAlarm.alarmHour)
    alarmMinList.append(setAlarm.alarmMin)

print(alarmHourList)
#print("The alarm time is " + str(setAlarm.alarmHour) + ":" + str(setAlarm.alarmMin))
print("The time now is " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute))


#while True:
    #if(setAlarm.alarmHour == datetime.datetime.now().hour and setAlarm.alarmMin == datetime.datetime.now().minute):
        #print("BEEEE BOOOOOO BEEEEEE BOOOOOOOOOOOOOOOO!!!!!!")
        ##play cute videos or give tasks
        #break



###Task Type###










