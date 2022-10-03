"module"
from app.config import APP_PATH
from app.utils.decorators import try_catch
from yaml import Loader, load


@try_catch
def get(name):
    "function"
    res, status = template_db(name)
    if status != 200:
        return res, status
    data = load(res.encode("utf-8"), Loader=Loader)
    return data, 200


@try_catch
def get_yaml(name):
    "function"
    res, status = template_db(name)
    if status != 200:
        return res, status
    return res, 200


@try_catch
def template_db(template):
    "function"
    with open(APP_PATH + "db/templates/" + template + ".yaml", "r") as file:
        data = file.read()

    return data, 200
