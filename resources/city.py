from models import CityModel
from flask import abort, make_response, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from schemas import CitySchema
from db import db

blp = Blueprint("Cities", __name__, description="Operations on cities")


@blp.route("/city")
class CityList(MethodView):
    @blp.response(200, CitySchema(many=True))
    def get(self):
        return CityModel.query.all()
    
    @blp.arguments(CitySchema)
    @blp.response(201, CitySchema)
    def post(self, city_data):
        city = CityModel(**city_data)

        try: 
            db.session.add(city)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Ocorreu um erro.")

        return city
    
@blp.route("/city/<int:city_id>")
class CitiesList(MethodView):
    @blp.arguments(CitySchema)
    @blp.response(200, CitySchema)
    def put(self, city_data, city_id):
      city = CityModel.query.get(city_id)

      city_dto = {}

      if city is None: 
          return make_response(jsonify({"message": "Cidade não existente."}), 404)
      
      city.name = city_data["name"]
      city.state_abbreviation = city_data["state_abbreviation"]
      city.group_of_councilors = city_data["group_of_councilors"]

      city_dto = {
          "id": city.id,
          "name": city.name,
          "state_abbreviation": city.state_abbreviation,
          "group_of_councilors": city.group_of_councilors,
      }

      db.session.add(city)
      db.session.commit()

      return make_response(jsonify(city_dto), 200)
    
    @blp.response(200, CitySchema)
    def get(self, city_id):
        city = CityModel.query.filter(CityModel.id == city_id).first()

        if city is None:
            return make_response(jsonify({"message": "Cidade não existente."}), 404)
        
        city_dto = {
          "id": city.id,
          "name": city.name,
          "state_abbreviation": city.state_abbreviation,
          "group_of_councilors": city.group_of_councilors,
        }

        return make_response(jsonify(city_dto), 200)

    @blp.response(204)
    def delete(self, city_id):
        city = CityModel.query.filter(CityModel.id == city_id).first()

        if city is None:
            return make_response(jsonify({"message": "Cidade não existente."}), 404)
        
        try:
            db.session.delete(city)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Erro ao excluir cidade.")

        return make_response(jsonify({"message": "Cidade excluída com sucesso."}), 204)