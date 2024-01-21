from datetime import datetime, date
from Appointment import Appointments
from ServiceBay import ServiceBay


class Day:
    def __init__(self, date: datetime.date):
        self.date = date

        self.SB = [ServiceBay(date) for _ in range(10)]

        self.appts = []
    
    def isValidInsertion(self):
        availList = []
        compact = 0
        fullSize = 0
        medium = 0
        truckC1 = 0
        truckC2 = 0
        emptyBays = 10

        added = False
        

    def add_appointment(self, inAppt: Appointments):
        """Checks for availability in each service bay and adds to appointments and the appropriate service bay if space is available."""
        possibilities = []
        compact = 0
        fullSize = 0
        medium = 0
        truckC1 = 0
        truckC2 = 0
        emptyBays = 10

        added = False

        #Calculate all slot possibilities
        for bay in self.SB:
            #Check if appointment overlapps in that serviceBay
            allOverlaps = bay.overlaps()
            if len(allOverlaps) == 0:
                #There is only one slot configuration
                possibilities.append(SlotPossibility(allOverlaps, serviceBay= bay)) #configuration where appointment is placed in timeslot
            else:

                possibilities.append(SlotPossibility(allOverlaps, serviceBay= bay)) #configuration where overlapps are kept
                possibilities.append(SlotPossibility([], serviceBay= bay)) #configuration where appointment is placed in timeslot
        
        #Add the possibility of turning away the appointment
        possibilities.append(SlotPossibility())

        #Sort possiblities based on deadspace
        possibilities.sort(key = lambda x: x.deadSpace)

        #Get possibility with smallest deadspace and check if it could be a valid insertion
        
        for bay in self.SB:
            availList.append(bay.balanceOfCarType(inAppt))
        
        #For debugging
        #print(availList)
        #print(self.date)
        #print(inAppt.appt_start)
        #print(inAppt.appt_end)
        #print(self.appts)

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


        
        #For debugging
        #print(availList)
        #print(self.date)
        #print(inAppt.appt_start)
        #print(inAppt.appt_end)
        #print(self.appts)

        return bruh


class SlotPossibility:
    def __init__(self, appointment = None, overlaps = None, serviceBay = None):
            
            self.allOverlaps = overlaps
            self.serviceBay = serviceBay
            self.appointment = 
            self.deadSpace = self.calculateDeadSpace()
    
    def calculateDeadSpace(self):
        dS = 0 #In minutes
        end_times = [] #datetime objects of end times of appointments

        for i in range(len(self.serviceBay.appt)):
            if i == 0 and i == len(self.serviceBay.appt) - 1:
                dS_obj1 = self.serviceBay.appt[i].start_time_obj - datetime.strptime("7:00")
                dS_obj2 = datetime.strptime("19:00") - self.serviceBay.appt[i].end_time_obj
                dS += dS_obj1.minute + dS_obj2.minute
            elif i == 0:
                dS_obj1 = self.serviceBay.appt[i].start_time_obj - datetime.strptime("7:00") #left interval
                dS += dS_obj1.minute
                end_times.append(self.serviceBay.appt[i].end_time_obj) 
            elif i == len(self.serviceBay.appt) - 1:
                dS_obj1 = datetime.strptime("19:00") - self.serviceBay.appt[i].end_time_obj # left interval
                dS_obj2 = end_times.pop() - self.serviceBay.appt[i].start_time_obj # right interval
                dS += dS_obj1.minute +  dS_obj2.minute
            else:
                dS_obj1 = self.serviceBay.appt[i].start_time_obj - end_times.pop() #left interval
                dS += dS_obj1.minute
                end_times.append(self.serviceBay.appt[i].end_time_obj)
        self.deadSpace = dS
