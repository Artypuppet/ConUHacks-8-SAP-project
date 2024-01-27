from datetime import time, date, datetime, timedelta


class Appointments:
    def __init__(self, day, start, car):
        self.car_type = car
        self.car_rev = None
        self.status = "N/A"
        self.day = day
        self.appt_start = start  # Store the start time as a string
        # Convert start to a datetime object for calculation
        start_time_obj = datetime.strptime(start, '%H:%M')

        if car.lower() in ["compact", "medium", "full-size"]:
            end_time_obj = start_time_obj + timedelta(minutes=30)
            self.appt_end = str(end_time_obj).split(" ")[1][0:5]
            self.car_rev = 150
        elif car.lower() == "class 1 truck":
            end_time_obj = start_time_obj + timedelta(hours=1)
            self.appt_end = str(end_time_obj).split(" ")[1][0:5]
            self.car_rev = 250
        elif car.lower() == "class 2 truck":
            end_time_obj = start_time_obj + timedelta(hours=2)
            self.appt_end = str(end_time_obj).split(" ")[1][0:5]
            self.car_rev = 700

    def updateStatus(self, status):
        """Sets the status of the appointment to the specified state"""
        self.status = status
