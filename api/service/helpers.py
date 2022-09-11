"module"


def get_token_parser(api):
    "function"
    parser = api.parser()
    parser.add_argument(
        "Authorization",
        required=True,
        type=str,
        location="headers",
        help="API token",
    )
    return parser


def get_jwt_keys(keys):
    "function"
    key_obj = {}
    key_items = keys.split("||")
    for item in key_items:
        identity, value = item.split("=", 1)
        key_obj[identity] = value
    return key_obj
