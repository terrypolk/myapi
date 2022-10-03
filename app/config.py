"""
Common configuration settings
"""
import os

from dotenv import load_dotenv

from app import globalvars  # Not used here, just getting a path from it.

# Evaluate dynamic values.
APP_PATH = os.path.dirname(globalvars.__file__) + "/../"
GIT_PATH = APP_PATH + ".git"

# Load variables from config file.
load_dotenv(f"{APP_PATH}.env")
APP_URL = os.environ["APP_URL"]
DEBUG = os.environ["DEBUG"] == "true"
ENVIRONMENT = os.environ["ENVIRONMENT"]
JWTKEY_CURRENT = os.environ["JWTKEY_CURRENT"]
JWTKEYS = os.environ["JWTKEYS"]
SPA_TOKEN_HOURS = os.environ["SPA_TOKEN_HOURS"]
