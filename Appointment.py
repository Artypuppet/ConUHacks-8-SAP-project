from datetime import time, date, datetime, timedelta


class Appointments:
    def __init__(self, start, car):
        self.appt_start = start
        self.car_type = car
        self.appt_end = None
        self.car_rev = None
        self.status = "N/A"

        if car.lower() in ["compact", "medium", "full-size"]:
            self.appt_end = self.appt_start + str(timedelta(minutes=30))
            self.car_rev = 150
        elif car.lower() == "class 1 truck":
            self.appt_end = self.appt_start + str(timedelta(hours=1))
            self.car_rev = 250
        elif car.lower() == "class 2 truck":
            self.appt_end = self.appt_start + str(timedelta(hours=2))
            self.car_rev = 700

    def updateStatus(self, status):
        """Sets the status of the appointment to the specified state"""
        self.status = status
