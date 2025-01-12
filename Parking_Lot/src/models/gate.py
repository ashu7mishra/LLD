from Parking_Lot.src.models.base_model import BaseModel
from Parking_Lot.src.models.status.gate_status import GateStatus
from Parking_Lot.src.models.enum_types.gate_type import GateType


class Gate(BaseModel):

    def __init__(self, id:int, gate_number:int, gate_status:GateStatus, parking_lot, gate_type:GateType):
        super().__init__(id)
        self.gate_number = gate_number
        self.gate_status = gate_status
        self.parking_lot = parking_lot
        self.gate_type = gate_type