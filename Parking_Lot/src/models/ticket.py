from datetime import datetime

from Parking_Lot.src.models.base_model import BaseModel
from Parking_Lot.src.models.gate import Gate
from Parking_Lot.src.models.slot import Slot
from Parking_Lot.src.models.vehicle import Vehicle


class Ticket(BaseModel):

    def __init__(self, id:int, number:int, entry_time:datetime,
                 vehicle, generated_gate:Gate, parking_slot: Slot):
        super().__init__(id)
        self.number = number
        self.entry_time = entry_time
        self.vehicle = vehicle
        self.generated_gate = generated_gate
        self.parking_slot = parking_slot
