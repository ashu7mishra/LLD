from Parking_Lot.src.controller.ticket_controller import TicketController
from Parking_Lot.src.dtos.issueTokenRequest import IssueTokenRequest
from Parking_Lot.src.models.enum_types.vehicle_type import VehicleType
from Parking_Lot.src.repo.gate_repo import GateRepo
from Parking_Lot.src.repo.parking_lot_repo import ParkingLotRepo
from Parking_Lot.src.repo.slot_repo import SlotRepo
from Parking_Lot.src.repo.ticket_repo import TicketRepo
from Parking_Lot.src.repo.vehicle_repo import VehicleRepo
from Parking_Lot.src.service.ticket_service import TicketService

if __name__ == '__main__':

    gate_repo = GateRepo()
    vehicle_repo = VehicleRepo()
    slot_repo = SlotRepo()
    ticket_repo = TicketRepo()
    parking_lot_repo = ParkingLotRepo()

    ticket_service = TicketService(gate_repo, vehicle_repo, slot_repo, parking_lot_repo, ticket_repo)

    ticket_controller = TicketController(ticket_service)

    request = IssueTokenRequest(vehicle_number='1234',
                                owner_name='Manish',
                                gate_id=1,
                                vehicle_type=VehicleType.CAR)

    response = ticket_controller.issue_ticket(request)

    print(response.ticket_id)