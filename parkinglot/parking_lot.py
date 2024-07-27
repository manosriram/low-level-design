from level import Level
from vehicle import Vehicle


class ParkingLot:
    _instance = None

    def __init__(self) -> None:
        if ParkingLot._instance is not None:
            pass
        else:
            ParkingLot._instance = self
            self.levels = []

    @staticmethod
    def get_instance():
        return ParkingLot._instance

    def add_level(self, level: Level):
        self.levels.append(level)
        return self

    def park_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True

        return False


    def unpark_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True

        return False

    def display_availability(self):
        for level in self.levels:
            level.display_availability()
