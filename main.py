from Scheduler import Scheduler
import sys
sys.setrecursionlimit(15000)
print(sys.getrecursionlimit())
file = "datafile.csv"

scheduler = Scheduler(file)
scheduler.schedule()
