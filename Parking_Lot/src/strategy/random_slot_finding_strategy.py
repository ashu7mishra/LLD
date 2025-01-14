from Parking_Lot.src.models.enum_types.vehicle_type import VehicleType
from Parking_Lot.src.models.gate import Gate
from Parking_Lot.src.models.slot import Slot
from Parking_Lot.src.models.status.slot_status import SlotStatus
from Parking_Lot.src.strategy.slot_strategy import SlotStrategy


class RandomSlotFindingStrategy(SlotStrategy):

    def get_slots(self, vehicleType: VehicleType, gate: Gate):
        for floor in gate.parking_lot.parking_floors:
            if vehicleType in floor.allowed_vehicles:
                for slot in floor.parking_slots:
                    if slot.vehicle_type == vehicleType and slot.parking_slot_status == SlotStatus.PARKING:
                        return slot
        return None
