from .Observer import Observer
import sys


class Logger(Observer):

    def __init__(self):
        try:
            self.file = open("loggerfile.txt", "a")
        except:
            print("File could not open.", file=sys.stderr)
            print("Exiting program...")
            sys.exit(1)

    def update(self, appointment):
        try:
            self.file.write(appointment.appt_start+"," +
                            appointment.car_type+","+appointment.status+"\n")
        except:
            print("Could not write to loggerfile.txt", file=sys.stderr)
