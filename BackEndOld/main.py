from Scheduler import Scheduler
from Logger import Logger
from StatisticalTracker import StatisticalTracker

#sys.setrecursionlimit(15000)

file = "BackEnd/datafile.csv"

scheduler = Scheduler(file)

#Attach observers
scheduler.attach(Logger())
scheduler.attach(StatisticalTracker())

#Start process
scheduler.schedule()

print(StatisticalTracker.types)
