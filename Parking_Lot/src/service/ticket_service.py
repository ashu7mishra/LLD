from datetime import datetime
from Parking_Lot.src.models.ticket import Ticket
from Parking_Lot.src.models.vehicle import Vehicle


class TicketService:

    def __init__(self, GateRepo, VehicleRepo):
        self.gateRepo = GateRepo
        self.vehicleRepo = VehicleRepo

    def issueTicket(self, vehicle_number, owner_name, gate_id, vehicle_type) -> Ticket:

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



        """
            create a ticket
            set info like gate no etc
            find a slot
            update parking counters
            return ticket
        """