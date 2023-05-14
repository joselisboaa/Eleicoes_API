from db import db

class CityModel(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    state_abbreviation = db.Column(db.String(10), nullable=False)
    group_of_councilors = db.Column(db.Integer, nullable=False)
    
    electoral_zones = db.relationship("ElectoralZoneModel", back_populates="cities", lazy="dynamic", cascade="all, delete")