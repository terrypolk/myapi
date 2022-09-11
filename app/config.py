"""
Common configuration settings
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from app import globalvars  # Not used here, just getting a path from it.

# Load variables from config file.
load_dotenv(Path(os.environ["HOME"]) / ".env_app")
DEBUG = os.environ["DEBUG"] == "true"

# Evaluate dynamic values.
APP_PATH = os.path.dirname(globalvars.__file__)
GIT_PATH = APP_PATH + "/../.git"
