# Run:
# (to open) flask run
# (close)   ctrl+C

# Run continuously with docker:
# (create img)  docker build -t flask-smorest-api .
# (as daemon)   docker run -dp 5000:5000 -w //app -v "$(Get-Location)://app" flask-smorest-api
# (in terminal) docker run -p 5000:5000 -w //app -v "$(Get-Location)://app" flask-smorest-api
# (to see id)   docker container ls
# (to kill)     docker container kill <container-id>

# Swagger interactive documentation:
# http://localhost:5000/swagger-ui

# -----------------------------------

import os

from flask import Flask
from flask_smorest import Api

from db import db
import models

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"

    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv(
        "DATABASE_URL", "sqlite:///data.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    # DEPRECATED
    # @app.before_first_request
    # def create_tables():
    #     db.create_all()
    # So...

    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)

    return app
