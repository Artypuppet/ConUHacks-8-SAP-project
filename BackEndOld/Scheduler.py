from .Subject import Subject
from .Day import Day
import pandas as pd
from datetime import datetime
from datetime import date
from .Appointment import Appointments
import csv


class Scheduler(Subject):
    """[Attributes]
        -days: Stores the days of the month within a dictionary (only stores them if they are present within the csv file)
        -csvFile: Stores the customers' information inside a list
       [Methods]
        -loadFile(self,csvFileName): Loads the customers' information inside the csvFile
        -schedule(self): Tries to shedule """

    def __init__(self, csvFileName: str):
        # Calling parent constructor to initialize observers
        Subject.__init__(self)
        self.days = {}
        self.csvFile = []
        self.loadFile(csvFileName)

    def loadFile(self, csvFileName: str):
        with open(csvFileName, "r") as file:

            next(file)
            reader = csv.reader(file)

            for row in reader:
                self.csvFile.append(row)

    def schedule(self):
        self.sortCSVFileByRequestTime(0, len(self.csvFile) - 1)
        # print(len(self.csvFile)) For debugging
        # print(self.csvFile) For debugging
        for ind in range(len(self.csvFile)):
            year, month, day = self.csvFile[ind][0].split(' ')[0].split(
                "-")
            apptDate = date(int(year), int(month), int(day))

            # looking for timetravelers
            if (datetime.strptime(self.csvFile[ind][1], '%Y-%m-%d %H:%M') < datetime.strptime(self.csvFile[ind][0], '%Y-%m-%d %H:%M')):
                continue

            # If date does not exist in self.day, create a day object and store it at the days
            if apptDate not in self.days:
                self.days[apptDate] = Day(apptDate)

            # Create an appointment and try to add it to the schedule
            appointment = Appointments(self.csvFile[ind][1].split(" ")[
                                       1], self.csvFile[ind][2])

            if (self.days[apptDate].add_appointment(appointment)):
                appointment.status = 'Success'
            else:
                appointment.status = "Turnaway"
            self.notify(appointment)

    def sortCSVFileByRequestTime(self, low: int, high: int) -> None:
        if (low >= high):
            return None
        middle = int((low + high) / 2)
        self.sortCSVFileByRequestTime(low, middle)
        self.sortCSVFileByRequestTime(middle + 1, high)
        self.merge(low, middle, high)

    def merge(self, low: int, middle: int, high: int):
        left = self.csvFile[low: middle + 1]
        right = self.csvFile[middle + 1: high]
        i = 0
        j = 0
        k = low
        while i < len(left) and j < len(right):
            l = left[i][0]
            r = right[j][0]
            if (self.compareRequestTime(l, r)):
                self.csvFile[k] = left[i]
                i += 1
            else:
                self.csvFile[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            self.csvFile[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            self.csvFile[k] = right[j]
            k += 1
            j += 1

    def compareRequestTime(self, date1: str, date2: str):
        d1 = date1.split(' ')
        year, month, day = d1[0].split("-")
        hour, minute = d1[1].split(":")
        dateObj1 = datetime(int(year), int(
            month), int(day), int(hour), int(minute))
        d2 = date2.split(' ')
        year, month, day = d2[0].split("-")
        hour, minute = d2[1].split(":")
        dateObj2 = datetime(int(year), int(
            month), int(day), int(hour), int(minute))
        return dateObj1 < dateObj2
