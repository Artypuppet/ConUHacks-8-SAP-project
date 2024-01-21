from Scheduler import Scheduler
from Logger import Logger
from StatisticalTracker import StatisticalTracker
import json
import sys
#sys.setrecursionlimit(15000)

file = "./datafile.csv"

scheduler = Scheduler(file)

#Attach observers
scheduler.attach(Logger())
scheduler.attach(StatisticalTracker())

#Start process
scheduler.schedule()

try:
    with open("output.json", "w") as file:
        file.write(json.dumps(StatisticalTracker.types))
        file.write(json.dumps(StatisticalTracker.overallStats))
except:
    print("Could not print to JSON file.\nExiting program...", file = sys.stderr)
    sys.exit(1)