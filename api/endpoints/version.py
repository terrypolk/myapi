"module"
from api.config import GIT_VERSION
from api.service.schemas import VersionSchema
from app.config import APP_URL
from flask_restplus import Resource

API = VersionSchema.api


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
