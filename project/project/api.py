from datetime import datetime

from ninja import NinjaAPI
from ninja.renderers import JSONRenderer
from ninja.responses import NinjaJSONEncoder
from ticket.views.views import router as ticket_router
from utils.exceptions import (
    BadRequest,
    ContentConflict,
    ContentDoesNotExist,
    ForbiddenContent,
    HttpVersionNotSupported,
)


class JsonEncoder(NinjaJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%SZ")

        return super().default(obj)


class GlobalJsonRenderer(JSONRenderer):
    encoder_class = JsonEncoder


api = NinjaAPI(renderer=GlobalJsonRenderer())

"""
    Exception Handler for Presentation Layer.
    It handles raised exception from another layer on purpose
    to present errors to client with HTTP status code.
    So most of the time, errors handled by this function should not be
    handled by other layers.
"""
FACTORY = {
    BadRequest: 400,
    ForbiddenContent: 403,
    ContentDoesNotExist: 404,
    ContentConflict: 409,
    HttpVersionNotSupported: 505,
}


@api.exception_handler(Exception)
def exception_handler(request, exception):
    if type(exception) not in FACTORY.keys():
        return api.create_response(
            request,
            "알 수 없는 오류가 발생했습니다. 문제가 지속된다면, 관리자에게 문의해주세요.",
            status=500,
        )

    return api.create_response(request, str(exception), status=FACTORY[type(exception)])


api.add_router("tickets", ticket_router)
