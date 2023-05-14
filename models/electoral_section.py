from db import db

class ElectoralSectionModel(db.Model):
    __tablename__ = "electoral_sections"

    id = db.Column(db.Integer, primary_key=True)
    zone_id = db.Column(db.Integer, db.ForeignKey("electoral_zones.id"), nullable=False)
    name = db.Column(db.String(15), nullable=False, unique=True)

    electoral_zones = db.relationship("ElectoralZoneModel", back_populates="electoral_sections")
    votes = db.relationship("VoteModel", back_populates="electoral_sections")