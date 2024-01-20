import datetime as dt
from Appointment import Appointments
import Day


class ServiceBay:
    def __init__(self, day: dt.date, appt: Appointments):
        self.appt = []
        self.day = day

    def isOccupied(self, newAppt: Appointments) -> (bool, str):
        for existingAppt in self.appt:
            if (newAppt.appt_start >= existingAppt.appt_end or 
                newAppt.appt_end <= existingAppt.appt_start):
                return True, existingAppt.car_type
        return False, None
        

    
