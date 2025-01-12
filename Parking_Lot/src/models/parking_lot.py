from typing import List
from Parking_Lot.src.models.floor import Floor
from Parking_Lot.src.models.gate import Gate
from Parking_Lot.src.models.status.parking_lot_status import ParkingLotStatus
from Parking_Lot.src.models.enum_types.slot_assignment_strategy_enum import SlotAssignmentStrategyEnum
from Parking_Lot.src.models.enum_types.vehicle_type import VehicleType


class ParkingLot:
    def __init__(self, id:int, name:str, address:str, parking_floors:List[Floor], gates:List[Gate],
                 allowed_vehicles:List[VehicleType], capacity:int, status:ParkingLotStatus,
                 slot_assignment_strategy:SlotAssignmentStrategyEnum):
        super().__init__(id)
        self.name = name
        self.address = address
        self.parking_floors = parking_floors
        self.gates = gates
        self.allowed_vehicles = allowed_vehicles
        self.capacity = capacity
        self.status = status
        self.slot_assignment_strategy = slot_assignment_strategy