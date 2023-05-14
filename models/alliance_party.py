from db import db 

class AlliencePartyModel(db.Model):
    __tablename__ = "alliences_party"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False, unique=True)
    
    parties = db.relationship("PartyModel", back_populates="alliences_party", lazy="dynamic", cascade="all, delete")