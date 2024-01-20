from Subject import Subject
from Day import Day
from StatisticalTracker import StatisticalTracker
import pandas as pd
from datetime import date

class Scheduler(Subject):

    def __init__(self, csvFileName: str, statTracker: StatisticalTracker):
        self.days = {}
        self.csvFile = pd.read_csv(csvFileName)
        self.statTracker = StatisticalTracker()
        

    def schedule(self, appointment):
        self.csvFile.sort()
        for row in self.csvFile:
            row 
    def sortCSVFileByRequestTime(self, low: int, high: int)-> None:
        if(low >= high):
            return None
        middle = low + high / 2
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
            if(self.compareRequestTime(left[0][i], right[0][j]))
                self.csvFile.iloc[k] = left[i]
                k += 1
                i += 1
            else:
                self.csvFile.iloc[k] = right[j]
                k += 1
                j += 1
        while i < len(left):
            self.csvFile.iloc[k] = left[i]
            k += 1
            i += 1
        
        while j < len(right):
            self.csvFile.iloc[k] = right[j]
            k += 1
            j += 1

        
    def compareRequestTime(self, date1:str, date2: str):
        year, month, day = date1.split(' ')[0].split("-")
        dateObj1 = date(int(year), int(month), int(day))
        year, month, day = date2.split(' ')[0].split("-")
        dateObj2 = date(int(year), int(month), int(day))
        return dateObj1 < dateObj2
        