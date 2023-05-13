import os
from flask import Flask
from flask_smorest import Api
from db import db
import models

def create_app():
      
  app = Flask(__name__)

  app.config["PROPAGATE_EXCEPTIONS"] = True
  app.config["API_TITLE"] = "Election REST API"
  app.config["API_VERSION"] = "v1"
  app.config["OPENAPI_VERSION"] = "3.0.3"
  app.config["OPENAPI_URL_PREFIX"] = "/"
  app.config["OPENAPI_SWAGGER_UI_PATH"] = "/api"
  app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
  app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

  api = Api(app)

  return app