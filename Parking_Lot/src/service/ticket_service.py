from datetime import datetime

from Parking_Lot.src.models.status.slot_status import SlotStatus
from Parking_Lot.src.models.ticket import Ticket
from Parking_Lot.src.models.vehicle import Vehicle
from Parking_Lot.src.strategy.get_slot_factory import SlotFactory


class TicketService:

    def __init__(self, GateRepo, VehicleRepo, slotRepo,
                 parkingLotRepo, ticketRepo):
        self.gateRepo = GateRepo
        self.vehicleRepo = VehicleRepo
        self.slotRepo = slotRepo
        self.parkingLotRepo = parkingLotRepo
        self.ticketRepo = ticketRepo

    def issueTicket(self, vehicle_number, owner_name, gate_id, vehicle_type) -> Ticket:

        """
                    create a ticket
                    set info like gate no etc
                    find a slot
                    update parking counters
                    return ticket
                """

        # create a ticket
        ticket = Ticket(id=-1, number="", entry_time=datetime.now(), vehicle=None, generated_gate=None, parking_slot=None)

        # set info like gate no etc
        gate = self.gateRepo.find_gate_by_id(gate_id)
        if gate == None:
            raise Exception("Gate not found")
        ticket.generated_gate = gate

        #vehicle info
        vehicle = self.vehicleRepo.find_vehicle_by_id(vehicle_number)
        if vehicle == None:
            vehicle = Vehicle(id=vehicle_number, owner_name=owner_name, vehicle_type=vehicle_type)
            vehicle = self.vehicleRepo.save_vehicle(vehicle)
        ticket.vehicle = vehicle

        #find a slot
        slot_stgy = SlotFactory.get_slot_strategy(gate.parking_slot.slot_assignment_strategy)

        if not slot_stgy:
            raise Exception("Slot assignment strategy not found")

        slot = slot_stgy.get_slot(vehicle.vehicle_type, gate)

        if not slot:
            raise Exception("Slot not found")

        ticket.parking_slot = slot

        # update slot

        self.slotRepo.update_slot_status(slot, SlotStatus.FILLED)

        # update parking counters
        self.parkingLotRepo.update_parking_lot_count(gate.parking_lot)

        #return ticket

        return self.ticketRepo.save_ticket(ticket)

