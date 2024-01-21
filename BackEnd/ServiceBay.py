import datetime as dt
import bisect
from Appointment import Appointments


class ServiceBay:
    def __init__(self, day: dt.date):
        self.appt = []
        self.day = day

    def addAppointment(self, new_appt: Appointments):
        position = bisect.bisect_left(self.appt, new_appt)
        self.appt.insert(position, new_appt)

    def balanceOfCarType(self, Appt: Appointments):
        for existingAppt in self.appt:
            if (Appt.appt_start < existingAppt.appt_end or
                    Appt.appt_end > existingAppt.appt_start):
                return existingAppt.car_type
            return 'Empty'
