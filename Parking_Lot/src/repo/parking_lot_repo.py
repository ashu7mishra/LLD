from Parking_Lot.src.models.parking_lot import ParkingLot


class ParkingLotRepo:

    def __init__(self):
        self.parkinglots = {}


    def update_parking_lot_count(self, parking_lot: ParkingLot):
        parking_lot.capacity -= 1
        self.parkinglots[parking_lot.id] = parking_lot
        return parking_lot