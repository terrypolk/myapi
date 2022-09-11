# pylint: disable=no-self-use
"module"
from api.config import GIT_VERSION
from api.service.schemas import VersionSchema
from flask_restplus import Resource

# from app.config import LCS_URL

API = VersionSchema.api
APP_URL = "localhost"


@API.route("/")
class Version(Resource):
    "class"

    def get(self):
        """
        Get API version
        """
        return {
            "data": {
                "version": GIT_VERSION,
                "url": APP_URL + "/api",
                "source": "https://github.com/terrypolk/myapi",
            }
        }, 200
