from db import db

class VoteModel(db.Model):
  __tablename__ = "votes"

  id = db.Column(db.Integer, primary_key=True)
  section_id = db.Column(db.Integer, db.ForeignKey("electoral_sections"), nullable=False, required=True)
  # In case of null vote the id is Null (will need a constraint which will verify if voted number exists)
  candidate_mayor_id = db.Column(db.Integer, db.ForeignKey("candidates"), nullable=True)
  candidate_councilman_id = db.Column(db.Integer, db.ForeignKey("candidates"), nullable=True)
  blank_vote = db.Column(db.Boolean)
  null_vote = db.Column(db.Boolean)

  section = db.relationship("ElectoralSectionModel", backpopulates="votes")
  candidate_mayor = db.relationship("CandidateModel", backpopulates="votes")
  candidate_councilman = db.relationship("CandidateModel", backpopulates="votes")