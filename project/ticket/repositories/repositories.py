from base.repositories.repositories import BaseModelRepository

from ..models.models import Ticket


class TicketModelRepository(BaseModelRepository):
    def __init__(self):
        self.model = Ticket
