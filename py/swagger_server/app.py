import connexion

from swagger_server import encoder
from connexion.exceptions import BadRequestProblem
from connexion.apis.flask_api import FlaskApi
from flask import Flask, got_request_exception
from werkzeug.exceptions import MethodNotAllowed
from connexion.problem import problem


def error_method_not_allowed(exception):
    return FlaskApi.get_response(
        problem(
            status=exception.code,
            title="Invalid input",
            detail=exception.description,
            headers={"Allow": "POST"},
        )
    )


def create_app():
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        "swagger.yaml",
        arguments={"title": "Mercedes-Benz AG Programming Challenge"},
        validate_responses=True,
    )
    app.add_error_handler(MethodNotAllowed, error_method_not_allowed)
    return app
