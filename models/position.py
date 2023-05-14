from db import db

class PositionModel(db.Model):
    __tablename__ = "positions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    
    candidates = db.relationship("CandidateModel", back_populates="positions", lazy="dynamic", cascade="all, delete")