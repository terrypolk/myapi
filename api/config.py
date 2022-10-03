# pylint: disable=too-few-public-methods
"module"
from app.config import DEBUG, JWTKEYS
from app.shell import repo_info

from api.service.helpers import get_jwt_keys

# Evaluated here
GIT_TAG, GIT_VERSION = repo_info()
JWTKEY = get_jwt_keys(JWTKEYS)


class FlaskAppConfig:
    "class"
    RESTPLUS_JSON = {}
    ERROR_404_HELP = False
    DEBUG = DEBUG
