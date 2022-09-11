# pylint: disable=global-variable-undefined
"module"


def init():
    "function"
    global BLACKLIST
    BLACKLIST = []

    global LAST_EMAIL_ALERT
    LAST_EMAIL_ALERT = {"BLACKLIST": 0, "JWKS": 0, "NEWGROUPS": 0}
