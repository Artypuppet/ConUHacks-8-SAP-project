from Subject import Subject
from Day import Day
import pandas as pd
from datetime import datetime
from datetime import date
from Appointment import Appointments
import csv


class Scheduler(Subject):

    def __init__(self, csvFileName: str):
        self.days = {}
        self.csvFile = []
        self.loadFile(csvFileName)

    def loadFile(self, csvFileName):
        with open(csvFileName, "r") as file:
            next(file)
            reader = csv.reader(file)
            self.csvFile = []
            for row in reader:
                self.csvFile.append(row)

    def schedule(self):
        self.sortCSVFileByRequestTime(0, len(self.csvFile) - 1)
        print(len(self.csvFile))
        print(self.csvFile)
        for ind in range(len(self.csvFile)):
            year, month, day = self.csvFile[ind][0].split(' ')[0].split(
                "-")
            apptDate = date(int(year), int(month), int(day))
            if apptDate not in self.days:
                self.days[apptDate] = Day(apptDate)
            appointment = Appointments(
                self.csvFile[1][ind], self.csvFile[2][ind])
            if (self.days[apptDate].add_appointment(appointment)):
                appointment.status = 'Success'
                self.Notify(appointment)
            else:
                appointment.status = "Turnaway"

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
