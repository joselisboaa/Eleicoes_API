from db import db 
# Relationship must be a many to many #
class AllienceParty(db.Model):
    __tablename__ = "alliences_party"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), required=True, nullable=False, unique=True)
    