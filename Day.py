import datetime as dt
from Appointment import Appointments
from ServiceBay import ServiceBay


class Day:
    def __init__(self, date: dt.date):
        self.date = date
        self.SB = [ServiceBay(date) for _ in range(10)]
        self.appts = []

    def add_appointment(self, appt: Appointments):
        """Checks for availability in each service bay and adds to appointments and the appropriate service bay if space is available."""

        added = False
        for bay in self.SB:
            if not bay.isOccupied(appt):
                bay.appt.append(appt)
                self.appts.append(appt)
                added = True
                break
        return added
