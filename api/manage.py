"module"
from flask_script import Manager

from api.main import create_app

APP = create_app()
MANAGER = Manager(APP)


@MANAGER.command
def run():
    "function"
    APP.run(port=5555, host="0.0.0.0")


if __name__ == "__main__":
    MANAGER.run()
