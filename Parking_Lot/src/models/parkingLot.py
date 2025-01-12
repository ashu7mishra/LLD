from Parking_Lot.src.models.floor import Floor
from Parking_Lot.src.models.gate import Gate


class ParkingLot:
    def __init__(self):
        self.id = None
        self.name = None
        self.address = None
        self.capacity = None
        self.floor = Floor
        self.entry_gate = Gate()
        self.exit_gate = Gate()
        self.timing = None
        self.allowed_vehicle_type = None
        self.status = None
        self.fee_calculation_strategy = None
        self.slot_picking_strategy = None