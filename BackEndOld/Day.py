from datetime import datetime, date
from .Appointment import Appointments
from .ServiceBay import ServiceBay


class Day:
    def __init__(self, date: datetime.date):
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

        # For debugging
        # print(availList)
        # print(self.date)
        # print(inAppt.appt_start)
        # print(inAppt.appt_end)
        # print(self.appts)

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

        if (compact == 0 and inAppt.car_type not in 'compact'):
            emptyBays = emptyBays - 1
        if (fullSize == 0 and inAppt.car_type not in 'full-size'):
            emptyBays = emptyBays - 1
        if (medium == 0 and inAppt.car_type not in 'medium'):
            emptyBays = emptyBays - 1
        if (truckC1 == 0 and inAppt.car_type not in 'class 1 truck'):
            emptyBays = emptyBays - 1
        if (truckC2 == 0 and inAppt.car_type not in 'class 2 truck'):
            emptyBays = emptyBays - 1

        if (emptyBays > 0):
            for i, type in enumerate(availList):
                if type in ['Empty']:
                    self.SB[i].appt.append(inAppt)
                    self.appts.append(inAppt)
                    added = True
                    break

        return added
