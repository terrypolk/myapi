"module"
from api.service.decorators import token_required
from api.service.schemas import TemplatesSchema
from app.db import templates
from flask import request
from flask_restplus import Resource

API = TemplatesSchema.api


@API.route("/", doc=False)
class TemplateGet(Resource):
    "class"

    @token_required
    def get(self):
        "function"
        name = request.args.get("Name")
        if not name:
            return {"error": "Missing required param: Name"}, 400

        res, status = templates.get(name)
        if status != 200:
            return res, status

        return {"Data": res}, 200


@API.route("/<template_name>", doc=False)
class TemplateGetRecord(Resource):
    "class"

    @token_required
    def get(self, template_name):
        "function"
        res, status = templates.get(template_name)
        if status != 200:
            return res, status
        return {"Data": res}, 200
