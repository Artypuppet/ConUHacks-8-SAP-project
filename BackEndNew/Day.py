from datetime import datetime, date, timedelta
from re import L
from Appointment import Appointments
from ServiceBay import ServiceBay


class Day:
    def __init__(self, date: datetime.date):
        self.date = date

        self.SB = [ServiceBay(date) for _ in range(10)]

        self.appts = []
    
    def isValidInsertion(self,inAppt):
        availList = []
        insertList = []
        compact = 0
        fullSize = 0
        medium = 0
        truckC1 = 0
        truckC2 = 0
        emptyBays = 10

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

        insertList = availList

        #finding which bays are allowed to be used
        for x in insertList:
            if x in 'compact' and compact > 1 or compact == 1 and inAppt.car_type is 'compact':
                x = 1
            elif x in 'medium' and medium > 1 or medium == 1 and inAppt.car_type is 'medium':
                x = 1
            elif x in 'full-size' and fullSize > 1 or fullSize == 1 and inAppt.car_type is 'full-size':
                x = 1
            elif x in 'class 1 truck' and truckC1 > 1 or truckC1 == 1 and inAppt.car_type is'class 1 truck':
                x = 1
            elif x in 'compact' and compact > 1 or truckC2 == 1 and inAppt.car_type is 'class 2 truck':
                x = 1
            else:
                x = 0
            

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
        if emptyBays > 0:
            return (True, insertList)
        return (False, insertList)



    def add_appointment(self, inAppt: Appointments):
        """Checks for availability in each service bay and adds to appointments and the appropriate service bay if space is available."""
        possibilities = []
        compact = 0
        fullSize = 0
        medium = 0
        truckC1 = 0
        truckC2 = 0
        emptyBays = 10
        availList = []
        

        added = False
        #If the appointment is a walk-in, we always do brute-force solution
        if inAppt.walkIn == True:
            if (self.isValidInsertion(inAppt)[0]):
                for i, type in enumerate(availList):
                    if type in ['Empty']:
                        self.SB[i].appt.append(inAppt)
                        self.appts.append(inAppt)
                        added = True
                        break

                return added
            
        if (self.isValidInsertion[0]):
            for i, type in enumerate(availList):
                if type in ['Empty']:
                    self.SB[i].appt.append(inAppt)
                    self.appts.append(inAppt)
                    added = True
                    return added
        
        timeList = []

        for i, x in enumerate(self.isValidInsertion[1]):
            if x == 1:
                timeList[i] = self.SB[i].timeDifference(inAppt)
            elif x == 0:
                timeList[i] = timedelta.min

        maxtime = timeList[0]
        index = 0

        for i, x in enumerate(timeList):
            if timeList[i] > maxtime:
                maxtime = timeList[i]
                index = i
        
        overlap = self.SB[index].returnOverlappingAppointments(inAppt)

        self.SB[index].append(inAppt)
        added = True

        for appt in overlap:
            self.add_appointment(appt)
