from db import db

class PartyModel(db.Model):
    __tablaname__ = "parties"

    id = db.Column(db.Integer, primary_key=True)
    allience_party_id = db.Column(db.Integer, db.ForeignKey("alliences_party.id"))
    name = db.Column(db.String(255), nullable=False, required=True)
    abbreviation = db.Column(db.String(15), nullable=False, required=True)

    allience_party = db.relationship("AllienceParty", backpopulates="parties")