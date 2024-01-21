from datetime import datetime as dt, timedelta
from Appointment import Appointments

class ServiceBay:
    def __init__(self, day: dt.date):
        self.appt = []
        self.day = day

    def balanceOfCarType(self, Appt: Appointments):
        for existingAppt in self.appt:
            if (dt.strptime(Appt.appt_start, "%H:%M") < dt.strptime(existingAppt.appt_end, "%H:%M") and
                dt.strptime(Appt.appt_start, "%H:%M") > dt.strptime(existingAppt.appt_start, "%H:%M")) or (dt.strptime(Appt.appt_end, "%H:%M") < dt.strptime(existingAppt.appt_end, "%H:%M") and
                dt.strptime(Appt.appt_end, "%H:%M") > dt.strptime(existingAppt.appt_start, "%H:%M")):
                return existingAppt.car_type
        return 'Empty'
    
    def timeDifference(self, new_appt: Appointments):
        total_overlap_duration = timedelta(minutes=0)

        new_start = dt.strptime(new_appt.appt_start, "%H:%M")
        new_end = dt.strptime(new_appt.appt_end, "%H:%M")
        new_appt_duration = new_end - new_start

        for existing_appt in self.appt:
            existing_start = dt.strptime(existing_appt.appt_start, "%H:%M")
            existing_end = dt.strptime(existing_appt.appt_end, "%H:%M")

            # Check overlap and accumulate duration
            if (new_start < existing_end and new_end > existing_start):
                overlap_duration = min(existing_end, new_end) - max(existing_start, new_start)
                total_overlap_duration += overlap_duration

        if new_appt_duration > total_overlap_duration:
            # Return the time difference if the new appointment is longer
            return new_appt_duration - total_overlap_duration
        else:
            # Return an invalid marker if not
            return None
    
    def returnOverlappingAppointments(self, new_appt: Appointments) -> list:
        overlapping_appointments = []
        new_start = dt.strptime(new_appt.appt_start, "%H:%M")
        new_end = dt.strptime(new_appt.appt_end, "%H:%M")

        # Iterate in reverse to avoid indexing issues while removing items
        for i in reversed(range(len(self.appt))):
            existing_appt = self.appt[i]
            existing_start = dt.strptime(existing_appt.appt_start, "%H:%M")
            existing_end = dt.strptime(existing_appt.appt_end, "%H:%M")

            # Check overlap
            if (new_start < existing_end and new_end > existing_start):
                overlapping_appointments.append(self.appt.pop(i))  # Remove and add to the list

        return overlapping_appointments
