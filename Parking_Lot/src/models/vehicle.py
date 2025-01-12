from Parking_Lot.src.models.base_model import BaseModel
from Parking_Lot.src.models.vehicle_type import VehicleType


class Vehicle(BaseModel):
    def __init__(self, id:int, owner_name:str, vehicle_type:VehicleType):
        super().__init__(id)
        self.vehicle_type = vehicle_type
        self.owner_name = owner_name