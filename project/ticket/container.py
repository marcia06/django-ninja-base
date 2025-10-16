from dependency_injector import containers, providers

from .repositories.repositories import TicketModelRepository
from .services.services import (
    TicketCreateService,
    TicketDestroyService,
    TicketListService,
    TicketPartialUpdateService,
    TicketRetrieveService,
    TicketUpdateService,
)


class Container(containers.DeclarativeContainer):
    repository = providers.Factory(TicketModelRepository)

    ticket_retrieve_service = providers.Factory(
        TicketRetrieveService,
        repository=repository,
    )
    ticket_list_service = providers.Factory(
        TicketListService,
        repository=repository,
    )
    ticket_create_service = providers.Factory(
        TicketCreateService,
        repository=repository,
    )
    ticket_update_service = providers.Factory(
        TicketUpdateService,
        repository=repository,
    )
    ticket_partial_update_service = providers.Factory(
        TicketPartialUpdateService,
        repository=repository,
    )
    ticket_destroy_service = providers.Factory(
        TicketDestroyService,
        repository=repository,
    )
