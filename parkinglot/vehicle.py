from abc import ABC, abstractmethod

from enums import VehicleType

class Vehicle(ABC):
    def __init__(self, vehicle_type, license_plate_number) -> None:
        super().__init__()
        self.license_place_number = license_plate_number
        self.vehicle_type = vehicle_type

    @abstractmethod
    def type(self) -> VehicleType:
        pass

class Car(Vehicle):
    def __init__(self, license_plate_number) -> None:
        super().__init__(VehicleType.CAR, license_plate_number)

    def type(self) -> VehicleType:
        return VehicleType.CAR

class Truck(Vehicle):
    def __init__(self, license_plate_number) -> None:
        super().__init__(VehicleType.TRUCK, license_plate_number)

    def type(self) -> VehicleType:
        return VehicleType.TRUCK

class MotorCycle(Vehicle):
    def __init__(self, license_plate_number) -> None:
        super().__init__(VehicleType.MOTORCYCLE, license_plate_number)

    def type(self) -> VehicleType:
        return VehicleType.MOTORCYCLE
