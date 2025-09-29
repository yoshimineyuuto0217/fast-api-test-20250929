from enum import IntEnum


class StatusCodes(IntEnum):
    # 400番台
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_PERMISSION = 403
    NOT_FOUND = 404

    # 500番台
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502