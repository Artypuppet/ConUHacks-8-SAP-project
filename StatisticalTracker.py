import Observer
class StatisticalTracker(Observer):

    def __init__(self):
        self.totalRevenue = 0
        self.totalRevenueLoss = 0
        self.totalAppointmentNum = 0
        self.totalTurnawayNum = 0
    
    def update(self, statement: str):
        