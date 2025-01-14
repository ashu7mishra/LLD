from Parking_Lot.src.models.enum_types.slot_assignment_strategy_enum import SlotAssignmentStrategyEnum
from Parking_Lot.src.strategy.random_slot_finding_strategy import RandomSlotFindingStrategy


class SlotFactory:

    @staticmethod
    def get_slot_strategy(slotStrgyEnum):
        if slotStrgyEnum == SlotAssignmentStrategyEnum.RANDOM:
            return RandomSlotFindingStrategy()
