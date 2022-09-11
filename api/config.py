# pylint: disable=too-few-public-methods
"module"
from app.config import DEBUG
from app.shell import repo_info

# from .service.helpers import get_jwt_keys

# Evaluated here
# JWTKEY = get_jwt_keys(JWTKEYS)
GIT_TAG, GIT_VERSION = repo_info()

# Declared here
# BLACKLIST_CHECK_INTERVAL = 300


class FlaskAppConfig:
    "class"
    RESTPLUS_JSON = {}
    ERROR_404_HELP = False
    DEBUG = DEBUG
