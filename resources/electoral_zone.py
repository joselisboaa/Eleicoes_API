from models import ElectoralZoneModel, CityModel
from flask import abort, make_response, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from schemas import ElectoralZoneSchema, PlainElectoralZoneSchema
from db import db

blp = Blueprint("Electoral_zone", __name__, "Operations on electoral zones")

@blp.route("/zone")
class ZoneList(MethodView):
    @blp.response(200, ElectoralZoneSchema(many=True))
    def get(self):
        return ElectoralZoneModel.query.all()
    
    @blp.arguments(ElectoralZoneSchema)
    @blp.response(201, ElectoralZoneSchema)
    def post(self, zone_data):
        zones = ElectoralZoneModel(**zone_data)

        if ElectoralZoneModel.query.filter(ElectoralZoneModel.zone == zone_data["zone"]).first():
            return make_response(jsonify({"message": "Zona já cadastrada."}))

        try:
            db.session.add(zones)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Erro ao inserir zona.")

        return zones
    
@blp.route("/zone/<int:zone_id>")
class ZonesList(MethodView):
    @blp.response(200, ElectoralZoneSchema)
    def get(self, zone_id):
        zone = ElectoralZoneModel.query.filter(ElectoralZoneModel.id == zone_id).first()

        if zone is None:
            return make_response(jsonify({"message": "Zona não existente."}))
        
        city = CityModel.query.filter(CityModel.id == zone.city_id).first()
        
        # should have votes
        zone_dto = {
            "id": zone.id,
            "zone": zone.zone, 
            "city": {
                "id": city.id,
                "name": city.name,
                "state_abbreviation": city.state_abbreviation,
                "group_of_councilors": city.group_of_councilors,
            },
            "electoral_sections": []
        }

        # relationship not implemented yet
        for section in zone.electoral_sections:
            zone_dto["electoral_sections"].append(section)

        return make_response(jsonify(zone_dto))

    @blp.arguments(PlainElectoralZoneSchema)
    @blp.response(200, ElectoralZoneSchema)
    def put(self, zone_data, zone_id):
        zone = ElectoralZoneModel.query.filter(ElectoralZoneModel.id == zone_id).first()

        if zone is None:
            return make_response(jsonify({"message": "Zona não existente."}), 404)
        
        zone.zone = zone_data["zone"]

        db.session.add(zone)
        db.session.commit()

        city = CityModel.query.filter(CityModel.id == zone.city_id).first()
        
        # should have votes
        zone_dto = {
            "id": zone.id,
            "zone": zone.zone, 
            "city": {
                "id": city.id,
                "name": city.name,
                "state_abbreviation": city.state_abbreviation,
                "group_of_councilors": city.group_of_councilors,
            },
            "electoral_sections": []
        }

        return make_response(jsonify(zone_dto))
    
    @blp.response(204)
    def delete(self, zone_id):
        zone = ElectoralZoneModel.query.filter(ElectoralZoneModel.id == zone_id).first()

        if zone is None:
            return make_response(jsonify({"message": "Zona não existente."}), 404)
        
        try:
            db.session.delete(zone)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="Erro ao deletar zona.")

        return make_response(jsonify({"message": "Zona excluída com sucesso."}), 204)
        