class GlobalError(Exception):
    default_message: str | None = None

    def __init__(self, message: str | None = None):
        super().__init__()

        if message:
            self.message = message
        else:
            self.message = self.default_message

    def __str__(self):
        return self.message


class BadRequest(GlobalError):
    default_message = "잘못된 요청입니다."


class ForbiddenContent(GlobalError):
    default_message = "허용되지 않은 접근입니다."


class ContentDoesNotExist(GlobalError):
    default_message = "존재하지 않는 콘텐츠입니다."


"""
    Conflict Error's messages are not be able to declared generally.
    So use this exception as fit to the case.
"""


class ContentConflict(GlobalError):
    default_message = "Conflict Error"


class HttpVersionNotSupported(GlobalError):
    default_message = "지원하지 않는 버전입니다."
