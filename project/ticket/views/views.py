from typing import List

from ninja import Query, Router
from ninja.pagination import PageNumberPagination, paginate

from ..container import Container
from ..schemas.schemas import (
    TicketFilterSchema,
    TicketInSchema,
    TicketOutSchema,
    TicketPartialUpdateInSchema,
)
from ..services.services import (
    TicketCreateService,
    TicketDestroyService,
    TicketListService,
    TicketPartialUpdateService,
    TicketRetrieveService,
    TicketUpdateService,
)

router = Router()
container = Container()


@router.get("{ticket_id}", response=TicketOutSchema)
def retrieve(
    request,
    ticket_id: int,
) -> TicketOutSchema:
    service: TicketRetrieveService = container.ticket_retrieve_service()

    return service.retrieve(pk=ticket_id)


@router.get("", response=List[TicketOutSchema])
@paginate(PageNumberPagination, page_size=10)
def list(
    request,
    filters: Query[TicketFilterSchema],
) -> List[TicketOutSchema]:
    kwargs = filters.dict()
    if not kwargs["name"]:
        del kwargs["name"]

    service: TicketListService = container.ticket_list_service()

    return service.list(kwargs)


@router.post("", response={201: TicketOutSchema})
def create(
    request,
    data: TicketInSchema,
) -> TicketOutSchema:
    service: TicketCreateService = container.ticket_create_service()

    return service.create(data=data.dict())


@router.put("{ticket_id}", response=TicketOutSchema)
def update(
    request,
    ticket_id: int,
    data: TicketInSchema,
) -> TicketOutSchema:
    service: TicketUpdateService = container.ticket_update_service()

    return service.update(pk=ticket_id, data=data.dict())


@router.patch("{ticket_id}", response=TicketOutSchema)
def partial_update(
    request,
    ticket_id: int,
    data: TicketPartialUpdateInSchema,
) -> TicketOutSchema:
    service: TicketPartialUpdateService = container.ticket_partial_update_service()

    return service.partial_update(pk=ticket_id, data=data.dict(exclude_unset=True))


@router.delete("{ticket_id}", response={204: None})
def destroy(
    request,
    ticket_id: int,
) -> None:
    service: TicketDestroyService = container.ticket_destroy_service()
    service.destroy(pk=ticket_id)

    return 204, None
