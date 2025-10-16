from datetime import datetime

from ninja import FilterSchema, Schema


class TicketOutSchema(Schema):
    id: int
    name: str
    sasd: str
    created_at: datetime
    updated_at: datetime


class TicketInSchema(Schema):
    name: str


class TicketPartialUpdateInSchema(Schema):
    name: str | None = None


class TicketFilterSchema(FilterSchema):
    name: str | None = None
