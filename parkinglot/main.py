from level import Level
from parking_lot import ParkingLot
from vehicle import Car, MotorCycle, Truck


p = ParkingLot()
p.add_level(Level(1, 100)).add_level(Level(2, 50))

car1 = Car("ap31")
car2 = Car("ap32")
truck1 = Truck("tr1")
truck2 = Truck("tr2")
mcycle1 = MotorCycle("mcycle1")
mcycle2 = MotorCycle("mcycle2")

p.park_vehicle(car1)
p.park_vehicle(car2)

p.display_availability()

p.park_vehicle(truck1)
p.park_vehicle(truck2)

#  p.display_availability()

p.park_vehicle(mcycle1)
p.park_vehicle(mcycle2)

#  p.display_availability()
