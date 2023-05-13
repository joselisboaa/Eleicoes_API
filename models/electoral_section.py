from db import db

class ElectoralSectionModel(db.Model):
    __tablename__ = "electoral_sections"

    id = db.Column(db.Integer, primary_key=True)
    zone_id = db.Column(db.Integer, db.ForeignKey("electoral_zones.id"), nullable=False, required=True)
    name = db.Column(db.String(15), nullable=False, required=True, unique=True)

    zone = db.relationship("ElectoralZoneModel", backpopulates="electoral_sections")