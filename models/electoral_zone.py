from db import db

class ElectoralZoneModel(db.Model):
    __tablename__ = "electoral_zones"

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id"), unique=False, nullable=False, required=True)
    name = db.Column(db.String(15), unique=True, nullable=False, required=True)

    city = db.relationship("CityModel", backpopulates="electoral_zones")
