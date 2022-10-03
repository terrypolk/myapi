# pylint: disable=too-few-public-methods
"module"
from flask_restplus import Namespace


class AuthSchema:
    "class"
    api = Namespace("auth")


class TemplatesSchema:
    "class"
    api = Namespace("templates")


class VersionSchema:
    "class"
    api = Namespace("version", description="API version info")
