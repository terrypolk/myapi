"module"
from functools import wraps

from api.service.auth_service import validate_token
from flask import request


def token_required(fnc):
    "function"

    @wraps(fnc)
    def decorated(*args, **kwargs):
        data, status = validate_token(request.headers)
        if status != 200:
            return data, status
        return fnc(*args, **kwargs)

    return decorated
