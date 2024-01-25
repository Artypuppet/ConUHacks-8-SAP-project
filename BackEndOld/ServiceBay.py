from datetime import datetime as dt
from .Appointment import Appointments


class ServiceBay:
    def __init__(self, day: dt.date):
        self.appt = []
        self.day = day

    def balanceOfCarType(self, Appt: Appointments):
        for existingAppt in self.appt:
            if (dt.strptime(Appt.appt_start, "%H:%M") < dt.strptime(existingAppt.appt_end, "%H:%M") and
                dt.strptime(Appt.appt_start, "%H:%M") > dt.strptime(existingAppt.appt_start, "%H:%M")) or (dt.strptime(Appt.appt_end, "%H:%M") < dt.strptime(existingAppt.appt_end, "%H:%M") and
                                                                                                           dt.strptime(Appt.appt_end, "%H:%M") > dt.strptime(existingAppt.appt_start, "%H:%M")):
                return existingAppt.car_type
        return 'Empty'
