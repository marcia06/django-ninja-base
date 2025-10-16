from base.mixins.service_mixins import (
    CreateServiceMixin,
    DestroyServiceMixin,
    ListServiceMixin,
    PartialUpdateServiceMixin,
    RetrieveServiceMixin,
    UpdateServiceMixin,
)
from base.services.services import BaseService

from ..repositories.repositories import TicketModelRepository


class BaseTicketService(BaseService):
    def __init__(self, repository: TicketModelRepository) -> None:
        self.repository = repository


class TicketRetrieveService(BaseTicketService, RetrieveServiceMixin):
    pass


class TicketListService(BaseTicketService, ListServiceMixin):
    pass


class TicketCreateService(BaseTicketService, CreateServiceMixin):
    pass


class TicketUpdateService(BaseTicketService, UpdateServiceMixin):
    pass


class TicketPartialUpdateService(BaseTicketService, PartialUpdateServiceMixin):
    pass


class TicketDestroyService(BaseTicketService, DestroyServiceMixin):
    pass
