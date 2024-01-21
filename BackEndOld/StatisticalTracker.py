from BackEndOld.Observer import Observer


class StatisticalTracker(Observer):
    # compactCars, mediumCars, Full-SizeCars, Class1Trucks, Class2Trucks
    types = [{"totalRevenue": 0, "totalRevenueLoss": 0, "totalAppointmentNum": 0, "totalTurnawayNum": 0},
             {"totalRevenue": 0, "totalRevenueLoss": 0,
                 "totalAppointmentNum": 0, "totalTurnawayNum": 0},
             {"totalRevenue": 0, "totalRevenueLoss": 0,
                 "totalAppointmentNum": 0, "totalTurnawayNum": 0},
             {"totalRevenue": 0, "totalRevenueLoss": 0,
                 "totalAppointmentNum": 0, "totalTurnawayNum": 0},
             {"totalRevenue": 0, "totalRevenueLoss": 0, "totalAppointmentNum": 0, "totalTurnawayNum": 0}]
    overallStats = {"totalRevenue": 0, "totalRevenueLoss": 0,
                    "totalAppointmentNum": 0, "totalTurnawayNum": 0}

    def __init__(self):
        pass

    def update(self, appointment):
        if appointment.status == "Success":
            StatisticalTracker.overallStats["totalRevenue"] += appointment.car_rev
            StatisticalTracker.overallStats["totalAppointmentNum"] += 1

            carIndex = StatisticalTracker.getCarIndex(appointment.car_type)
            # Updates revenue stats for car
            StatisticalTracker.types[carIndex]["totalRevenue"] += appointment.car_rev
            # updates appointment num for car
            StatisticalTracker.types[carIndex]["totalAppointmentNum"] += 1

        elif appointment.status == "Turnaway":
            StatisticalTracker.overallStats["totalRevenueLoss"] -= appointment.car_rev
            StatisticalTracker.overallStats["totalTurnawayNum"] += 1

            carIndex = StatisticalTracker.getCarIndex(appointment.car_type)
            # Updates revenue stats for car
            StatisticalTracker.types[carIndex]["totalRevenueLoss"] -= appointment.car_rev
            # updates appointment num for car
            StatisticalTracker.types[carIndex]["totalTurnawayNum"] += 1
        elif appointment.status == "Rescheduled":
            # We have to subtract from the revenue because now we're at a loss
            StatisticalTracker.overallStats["totalRevenue"] -= appointment.car_rev
            StatisticalTracker.overallStats["totalRevenueLoss"] -= appointment.car_rev
            StatisticalTracker.overallStats["totalTurnawayNum"] += 1
            # We are only considering the number of appointments that we have scheduled therefore we need to update this
            StatisticalTracker.overallStats["totalAppointmentNum"] -= 1

            carIndex = StatisticalTracker.getCarIndex(appointment.car_type)

            StatisticalTracker.types[carIndex]["totalRevenue"] -= appointment.car_rev

            StatisticalTracker.types[carIndex]["totalRevenueLoss"] -= appointment.car_rev
            # updates appointment num for car
            StatisticalTracker.types[carIndex]["totalTurnawayNum"] += 1

            StatisticalTracker.types[carIndex]["totalAppointmentNum"] -= 1

    @staticmethod
    def getCarIndex(car):
        """Returns the index of the car type stored statically in StatisticalTracker"""
        if car == "compact":
            return 0
        elif car == "medium":
            return 1
        elif car == "full-size":
            return 2
        elif car == "class 1 truck":
            return 3
        elif car == "class 2 truck":
            return 4
