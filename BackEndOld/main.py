from .Scheduler import Scheduler
from .Logger import Logger
from .StatisticalTracker import StatisticalTracker
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
    return json.dumps(StatisticalTracker.types), json.dumps(StatisticalTracker.overallStats), json.dumps(StatisticalTracker.days)
