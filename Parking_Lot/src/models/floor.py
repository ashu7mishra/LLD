from typing import List

from Parking_Lot.src.models.base_model import BaseModel
from Parking_Lot.src.models.floor_status import FloorStatus
from Parking_Lot.src.models.vehicle_type import VehicleType


class Floor(BaseModel):

    def __init__(self, id:int, parking_slots_list:List, floor_number:int, allowed_vehicles:List[VehicleType], floor_status:FloorStatus):
        super().__init__(id)
        self.parking_slots_list = parking_slots_list
        self.floor_number = floor_number
        self.allowed_vehicles = allowed_vehicles
        self.floor_status = floor_status