from datetime import time, date, datetime, timedelta

class Appointments:
    def __init__(self, start, rev, car):
        self.appt_start = start
        self.car_type = car
        self.appt_end = None
        self.rev = None

        if car.lower() in ["compact", "medium", "full-size"]:
            self.appt_end = self.appt_start + timedelta(minutes=30)
            self.rev = 150
        elif car.lower() == "class 1 truck":
            self.appt_end = self.appt_start + timedelta(hours=1)
            self.rev = 250
        elif car.lower() == "class 2 truck":
            self.appt_end = self.appt_start + timedelta(hours=2)
            self.rev = 700
