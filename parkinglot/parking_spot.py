from enums import VehicleType
from vehicle import Vehicle


class ParkingSpot:
    def __init__(self, spot_number, vehicle_type) -> None:
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type
        self.vehicle = None

    def park_vehicle(self, vehicle: Vehicle):
        if self.is_available() and vehicle.type() == self.vehicle_type:
            self.vehicle = vehicle
        else:
            pass

    def unpark_vehicle(self):
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def get_parked_vehicle(self):
        return self.vehicle
