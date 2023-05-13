from db import db

class CandidateModel(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, required=True)
    number = db.Column(db.Integer, nullable=False, required=True, unique=True)
    position_id = db.Column(db.Integer, db.ForeignKey("positions.id"), required=True, nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey("parties.id"), required=True, nullable=False)

    party = db.relationship("PartyModel", backpopulates="candidates")
    position = db.relationship("PositionModel", backpopulates="candidates")