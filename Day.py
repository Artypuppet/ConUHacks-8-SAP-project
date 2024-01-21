import datetime as dt
from Appointment import Appointments
from BackEnd.ServiceBay import ServiceBay


class Day:
    def __init__(self, date: dt.date):
        self.date = date
        self.SB = [ServiceBay(date) for _ in range(10)]
        self.appts = [] 

    def add_appointment(self, inAppt: Appointments):
        """Checks for availability in each service bay and adds to appointments and the appropriate service bay if space is available."""
        availList = []
        compact = 0
        fullSize = 0
        medium = 0
        truckC1 = 0
        truckC2 = 0
        emptyBays = 10

        added = False
        for bay in self.SB:
            availList.append(bay.balanceOfCarType(inAppt))

        for type in availList:
            if type.lower in ['compact']:
                compact = compact + 1
                emptyBays = emptyBays - 1
            elif type.lower in ['medium']:
                medium = medium + 1
                emptyBays = emptyBays - 1
            elif type.lower in ['full-size']:
                fullSize = fullSize + 1
                emptyBays = emptyBays - 1
            elif type.lower in ['class 1 truck']:
                truckC1 = truckC1 + 1
                emptyBays = emptyBays - 1
            elif type.lower in ['class 2 truck']:
                truckC2 = truckC2 + 1
                emptyBays = emptyBays - 1

        if (compact == 0):
            emptyBays = emptyBays - 1
        if (fullSize == 0):
            emptyBays = emptyBays - 1
        if (medium == 0):
            emptyBays = emptyBays - 1
        if (truckC1 == 0):
            emptyBays = emptyBays - 1
        if (truckC2 == 0):
            emptyBays = emptyBays - 1

        if (emptyBays > 0):
            for type in availList:
                if type in ['Empty']:
                    bay.self.appt.append(inAppt)
                    added = True
                    break

        return added


