from abc import ABC, abstractmethod

from Parking_Lot.src.models.enum_types.vehicle_type import VehicleType
from Parking_Lot.src.models.gate import Gate
from Parking_Lot.src.models.slot import Slot


class SlotStrategy(ABC):

    @abstractmethod
    def get_slots(self, vehicleType: VehicleType, gate: Gate) -> Slot:
        pass
