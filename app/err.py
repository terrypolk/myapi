"""
Functions for error handling
"""
import sys
from pprint import pprint

from app.config import DEBUG


def err_obj(func_name, mod_name, error, **kwargs):
    "function"
    message = ""
    # "error" may be an Exception object or may be a string.
    if isinstance(error, Exception):
        message = "Error type: " + type(error).__name__ + ", " + str(error)
    else:
        message = "Error message: " + str(error)
    details = kwargs.get("details")
    status = kwargs.get("status", "error")
    # For API v2, these key name will be PascalCase.
    obj = {"status": status, "message": message, "error": message}  # remove in LCS 2.0
    if details:
        obj["details"] = details
    if DEBUG:
        obj["source"] = message + " in " + mod_name + ", function:" + func_name
    return obj


def fail(message):
    "function"
    pprint(message)
    sys.exit(1)
