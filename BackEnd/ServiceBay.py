import datetime as dt
import Appointment
import Day


class ServiceBay:
    def __init__(self, day: dt.date, appt: 'Appointment'):
        self.appt = []
        self.day = day

    def isOccupied(self, newAppt: 'Appointment') -> (bool, str):
        for existingAppt in self.appt:
            if (newAppt.appt_start < existingAppt.appt_end and 
                newAppt.appt_end > existingAppt.appt_start):
                return True, existingAppt.car_type
        return False, None
        
