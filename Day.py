import datetime as dt
from Appointment import Appointments
from BackEnd.ServiceBay import ServiceBay


class Day:
    def __init__(self, date: dt.date):
        self.date = date
        self.SB = [ServiceBay(date) for _ in range(10)]
        self.appts = [] 

    def add_appointment(self, appt: Appointments):
        """Checks for availability in each service bay and adds to appointments and the appropriate service bay if space is available."""
        availList = []
        compact = bool(0)
        fullSize = bool(0)
        medium = bool(0)
        truckC1 = bool(0)
        truckC2 = bool(0)
        emptyBays = 10

        added = False
        for bay in self.SB:
            availList.append(bay(balanceOfCarType(appt)))

        for type in availList:
            if type.lower in ['compact']:
                compact = bool(1)
                emptyBays = emptyBays - 1
            elif type.lower in ['medium']:
                medium = bool(1)
                emptyBays = emptyBays - 1
            elif type.lower in ['full-size']:
                fullSize = bool(1)
                emptyBays = emptyBays - 1
            elif type.lower in ['class 1 truck']:
                truckC1 = bool(1)
                emptyBays = emptyBays - 1
            elif type.lower in ['class 2 truck']:
                truckC2 = bool(1)
                emptyBays = emptyBays - 1

        

        for bay in self.SB:
            if not bay.isOccupied(appt):
                bay.appt.append(appt)
                self.appts.append(appt)
                added = True
                break
        return added


