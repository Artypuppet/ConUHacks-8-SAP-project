from datetime import datetime
from Appointment import Appointments
from BackEnd.ServiceBay import ServiceBay


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
        closeTime = datetime.time(19)
        startTime = datetime.strptime(inAppt.appt_start)
        endTime = datetime.strptime(inAppt.appt_end)
        emptyIndex = []
        deadTimeList = []
        added = False

        if (datetime.strptime(inAppt.appt_end , '%H:%M') > closeTime):
            return added
        

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

        if (emptyBays < 0)
            print('\n\n we fucked up \n\n')

        if (emptyBays > 0):
            for type in availList:
                if type in 'empty':
                    emptyIndex.append(availList.index(type))
                    deadTimeList.append(self.SB[availList.index(type)].getDeadTime())

            minDead = deadTimeList[0]        
            count = 0
            index = 0

            for time in deadTimeList:
                if time < minDead:
                    minDead = time
                    index = count
                count += 1
            self.SB[emptyIndex[index]].appt.append(inAppt)
            added = True
            return added
        

        elif (emptyBays == 0):
           added = recursiveOptimize(inAppt)

            


        
    
    def recursiveOptimize(self, inAppt: Appointments):
        deadTimeList = []
        for bay in self.SB:
            deadTimeList.append(bay.getDeadTime)
        




