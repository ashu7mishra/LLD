from Parking_Lot.src.dtos.issueTokenRequest import IssueTokenRequest
from Parking_Lot.src.dtos.ticket_response import TicketResponse
from Parking_Lot.src.service.ticket_service import TicketService


class TicketController:

    def __init__(self, ticketService: TicketService):
        self.ticketService = ticketService

    def issue_ticket(self, request:IssueTokenRequest) -> TicketResponse:
        ticket = self.ticketService.issueTicket(request.vehicle_number,
                                       request.owner_name,
                                       request.gate_id,
                                       request.vehicle_type)

        response = TicketResponse()
        response.ticket_id = ticket.number
        response.slot = ticket.parking_slot
        response.vehicle = ticket.vehicle.id
        response.entry_time = ticket.entry_time
        response.status = 'SUCCESS'
        return response
