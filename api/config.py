# pylint: disable=too-few-public-methods
"module"
from app.config import DEBUG
from app.shell import repo_info

# Evaluated here
GIT_TAG, GIT_VERSION = repo_info()


class FlaskAppConfig:
    "class"
    RESTPLUS_JSON = {}
    ERROR_404_HELP = False
    DEBUG = DEBUG
