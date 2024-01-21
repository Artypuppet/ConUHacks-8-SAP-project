from BackEndOld.Scheduler import Scheduler
from BackEndOld.Logger import Logger
from BackEndOld.StatisticalTracker import StatisticalTracker
import json
import sys
# sys.setrecursionlimit(15000)


def Driver(csvFilePath: str):
    file = csvFilePath

    scheduler = Scheduler(file)

    # Attach observers
    scheduler.attach(Logger())
    scheduler.attach(StatisticalTracker())

    # Start process
    scheduler.schedule()

    return json.dumps(StatisticalTracker.types), json.dumps(StatisticalTracker.overallStats)
