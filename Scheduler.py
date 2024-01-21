from Subject import Subject
from Day import Day
import pandas as pd
from datetime import date
from Appointment import Appointments


class Scheduler(Subject):

    def __init__(self, csvFileName: str):
        self.days = {}
        self.csvFile = pd.read_csv(csvFileName)

    def schedule(self):
        self.sortCSVFileByRequestTime(0, len(self.csvFile) - 1)
        self.csvFile.to_csv("output.csv")
        for ind in self.csvFile.index:
            year, month, day = self.csvFile.loc[ind, "Appointment"].split(' ')[0].split(
                "-")
            apptDate = date(int(year), int(month), int(day))
            if apptDate not in self.days:
                self.days[apptDate] = Day(apptDate)
            appointment = Appointments(
                self.csvFile["Appointment"][ind], self.csvFile["CarType"][ind])
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
        left = self.csvFile.loc[low: middle]
        right = self.csvFile.loc[middle + 1: high]
        i = low
        j = middle + 1
        k = low
        while i < len(left) and j < len(right):
            if (self.compareRequestTime(left[0][i], right[0][j])):
                self.csvFile.iloc[k] = left.iloc[i].copy()
                k += 1
                i += 1
            else:
                self.csvFile.iloc[k] = right.iloc[j].copy()
                k += 1
                j += 1
        while i < len(left):
            self.csvFile.iloc[k] = left.iloc[i].copy()
            k += 1
            i += 1

        while j < len(right):
            self.csvFile.iloc[k] = right.iloc[j].copy()
            k += 1
            j += 1

    def compareRequestTime(self, date1: str, date2: str):
        year, month, day = date1.split(' ')[0].split("-")
        dateObj1 = date(int(year), int(month), int(day))
        year, month, day = date2.split(' ')[0].split("-")
        dateObj2 = date(int(year), int(month), int(day))
        return dateObj1 < dateObj2
