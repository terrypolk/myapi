# pylint: disable=too-few-public-methods
"module"
import datetime

from flask_restplus import Namespace


class VersionSchema:
    "class"
    api = Namespace("version", description="API version info")
