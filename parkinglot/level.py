from parking_spot import ParkingSpot
from enums import VehicleType
from vehicle import Vehicle

class Level:
    def __init__(self, level_number, capacity) -> None:
        self.level_number = level_number
        self.capacity = capacity
        self.parking_spots = [ParkingSpot(i, VehicleType.CAR) if i%2 ==0 else ParkingSpot(i, VehicleType.MOTORCYCLE) for i in range(capacity)]

    def park_vehicle(self, vehicle: Vehicle):
        for parking_spot in self.parking_spots:
            if parking_spot.is_available() and parking_spot.vehicle_type == vehicle.type():
                parking_spot.park_vehicle(vehicle)
                print(f"parked {parking_spot.spot_number}")
                return True

        return False

    def unpark_vehicle(self, vehicle: Vehicle):
        for parking_spot in self.parking_spots:
            if not parking_spot.is_available() and parking_spot.get_parked_vehicle() == vehicle:
                parking_spot.unpark_vehicle()
                print(f"unparked {parking_spot.spot_number}")
                return True

        return False

    def display_availability(self):
        print("Available spots")
        for parking_spot in self.parking_spots:
            if parking_spot.is_available():
                print(f"{parking_spot.spot_number}", end=" ")
