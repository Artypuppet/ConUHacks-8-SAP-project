from datetime import datetime, time, date, timedelta
from Appointment import Appointments

class day:
    currentDay = None
    apptList = []
    def __init__(self, csvDate):
        dateList = csvDate.split(' ')
        self.currentDay = date.fromisoformat(csvDate[0])
        apptList = []

    def setAppt(self, carType, startTime):
        for x in self.apptList:
            occupied = bool(1)
            if x.appt_start <= startTime <= x.appt_end:
                occupied = bool(0)
                break
        if(occupied):
            newAppt = Appointments(startTime, 0, carType)
            self.apptList.append(newAppt)





        







        



       

            
            