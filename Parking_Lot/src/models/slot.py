from Parking_Lot.src.models.status.slot_status import SlotStatus
from Parking_Lot.src.models.enum_types.vehicle_type import VehicleType


class Slot:

    def __init__(self, id:int, slot_number:int, vehicle_type:VehicleType, parking_slot_status:SlotStatus, parking_floor:int):
        super().__init__(id)
        self.slot_number = slot_number
        self.vehicle_type = vehicle_type
        self.parking_slot_status = parking_slot_status
        self.parking_floor = parking_floor