from db import db

class ElectoralZoneModel(db.Model):
    __tablename__ = "electoral_zones"

    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey("cities.id"), unique=False, nullable=False)
    zone = db.Column(db.String(15), unique=True, nullable=False)

    cities = db.relationship("CityModel", back_populates="electoral_zones")
    electoral_sections = db.relationship("ElectoralSectionModel", back_populates="electoral_zones", lazy="dynamic", cascade="all, delete")