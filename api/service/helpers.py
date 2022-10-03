"module"


def get_jwt_keys(keys):
    "function"
    key_obj = {}
    key_items = keys.split("||")
    for item in key_items:
        identity, value = item.split("=", 1)
        key_obj[identity] = value
    return key_obj
