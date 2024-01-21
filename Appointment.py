from datetime import datetime, timedelta

class Appointments:
    def __init__(self, start, car):
        self.car_type = car
        self.car_rev = None
        self.status = "N/A"
        self.appt_start = start  # Store the start time as a string
        start_time_obj = datetime.strptime(start, '%H:%M')  # Convert start to a datetime object for calculation
        
        if car.lower() in ["compact", "medium", "full-size"]:
            end_time_obj = start_time_obj + timedelta(minutes=30)
            self.car_rev = 150
        elif car.lower() == "class 1 truck":
            end_time_obj = start_time_obj + timedelta(hours=1)
            self.car_rev = 250
        elif car.lower() == "class 2 truck":
            end_time_obj = start_time_obj + timedelta(hours=2)
            self.car_rev = 700
        
        # Convert the end time back to a string in the same format as appt_start
        self.appt_end = end_time_obj.strftime('%H:%M')

    def update_status(self, status):
        """Sets the status of the appointment to the specified state"""
        self.status = status

    def __lt__(self, other):
        """Compare appointments based on their start time for sorting"""
        return datetime.strptime(self.appt_start, '%H:%M') < datetime.strptime(other.appt_start, '%H:%M')
