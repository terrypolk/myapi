# pylint: disable=no-self-use
"module"
from api.service.auth_service import get_token, get_token_info
from api.service.decorators import token_required
from api.service.schemas import AuthSchema
from flask import request
from flask_restplus import Resource

API = AuthSchema.api


@API.route("/get-token", doc=False)
class AuthGetToken(Resource):
    "class"

    def get(self):
        "function"
        return get_token(request.headers)


@API.route("/token", doc=False)
class AuthTokenInfo(Resource):
    "class"

    @token_required
    def get(self):
        """
        Get details about the token you are currently using
        """
        return get_token_info(request.headers)
