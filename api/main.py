# pylint: disable=unused-variable,unused-argument
"module"

from app import globalvars
from flask import Blueprint, Flask, url_for
from flask_cors import CORS
from flask_restplus import Api, apidoc
from werkzeug.middleware.proxy_fix import ProxyFix

from api.config import GIT_TAG, GIT_VERSION, FlaskAppConfig
from api.endpoints.auth import API as auth
from api.endpoints.templates import API as templates
from api.endpoints.version import API as version


class MyCustomApi(Api):
    """
    Fix for Swagger UI path not using url_prefix.
    https://github.com/noirbizarre/flask-restplus/issues/517
    """

    def _register_apidoc(self, app: Flask) -> None:
        conf = app.extensions.setdefault("restplus", {})
        custom_apidoc = apidoc.Apidoc(
            "restplus_doc",
            "flask_restplus.apidoc",
            template_folder="templates",
            static_folder="static",
            static_url_path="/api",
        )

        @custom_apidoc.add_app_template_global
        def swagger_static(filename: str) -> str:
            return url_for("restplus_doc.static", filename=filename)

        if not conf.get("apidoc_registered", False):
            app.register_blueprint(custom_apidoc)
        conf["apidoc_registered"] = True


def create_app():
    "function"
    app = Flask(__name__)
    CORS(app)
    # Next line: https://github.com/noirbizarre/flask-restplus/issues/565
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.url_map.strict_slashes = False

    @app.errorhandler(404)
    def page_not_found(error):
        "function"
        return {"error": "path not found (or missing/incorrect path param?)"}, 404

    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api = MyCustomApi(
        blueprint,
        title="API",
        version=GIT_TAG,
        description=(f"Version: {GIT_VERSION}"),
    )

    api.add_namespace(auth)
    api.add_namespace(templates)
    api.add_namespace(version)
    app.register_blueprint(blueprint)
    app.config.from_object(FlaskAppConfig)
    app.app_context().push()

    globalvars.init()
    return app
