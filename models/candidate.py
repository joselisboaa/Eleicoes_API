from db import db

class CandidateModel(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)
    position_id = db.Column(db.Integer, db.ForeignKey("positions.id"), nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey("parties.id"), nullable=False)

    parties = db.relationship("PartyModel", back_populates="candidates")
    positions = db.relationship("PositionModel", back_populates="candidates")
    votes = db.relationship("VoteModel", back_populates="candidates")