"""
Miscellaneous lightweight helper functions - stuff that doesn't need other modules.
If you try to import other LCS modules into this file you'll probably get a cyclic import error.
"""


def get_token_from_headers(headers):
    "function"
    auth_token = headers.get("Authorization")
    token = auth_token
    if "Bearer " in token:
        parts = auth_token.split("Bearer ")
        if len(parts) == 2:
            token = parts[1]
    return token


def get_dag_id(request):
    "function"
    # Default workflow name is the request type with underscores instead of spaces.
    dag_id = request["requestType"].replace(" ", "_")

    # If this is a batch then don't look in the payload
    if isinstance(request["requestPayload"], list):
        return dag_id

    templates = request["requestPayload"].get("templates")
    if templates:
        this_template = templates.get(request["requestType"])
        if this_template:
            workflow = this_template.get("Workflow")
            if workflow:
                dag_id = workflow.replace(" ", "_")
    return dag_id


def get_support_mail_template(request):
    "function"
    support_mail_template = None
    request_payload = request["requestPayload"]
    templates = request_payload.get("templates")
    if templates:
        template = templates.get(request["requestType"])
        if template:
            support_mail_template = template.get("SupportMailTemplate")
    return support_mail_template


def get_server_people(server_data):
    """
    The infra/compute endpoint returns people details - take advantage of this by scraping
    everything you can.  You might be able to avoid a call to the SAD table.
    """
    props = ["FirstName", "LastName", "Email", "GlobalId"]
    folks = {}
    for role in ["SystemOwner", "SystemCustodian", "PrimaryItContact"]:
        role_data = server_data.get(role)
        if role_data:
            system_id = role_data.get("SystemId")
            if system_id:
                if folks.get(system_id):
                    continue
                folks[system_id] = {}
                for prop in props:
                    if role_data.get(prop):
                        folks[system_id][prop] = role_data.get(prop)

    for delegate in server_data.get("PatchDelegates"):
        system_id = delegate.get("SystemId")
        if system_id:
            if folks.get(system_id):
                continue
            folks[system_id] = {}
            for prop in props:
                if delegate.get(prop):
                    folks[system_id][prop] = delegate.get(prop)

    return folks
