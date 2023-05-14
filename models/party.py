from db import db

class PartyModel(db.Model):
    __tablename__ = "parties"

    id = db.Column(db.Integer, primary_key=True)
    allience_party_id = db.Column(db.Integer, db.ForeignKey("alliences_party.id"))
    name = db.Column(db.String(255), nullable=False, unique=True)
    abbreviation = db.Column(db.String(15), nullable=False, unique=True)

    alliences_party = db.relationship("AlliencePartyModel", back_populates="parties")
    candidates = db.relationship("CandidateModel", back_populates="parties", lazy="dynamic", cascade="all, delete")