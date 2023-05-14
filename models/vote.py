from db import db

class VoteModel(db.Model):
  __tablename__ = "votes"

  id = db.Column(db.Integer, primary_key=True)
  section_id = db.Column(db.Integer, db.ForeignKey("electoral_sections.id"), nullable=False)
  # In case of null vote the id is Null (will need a constraint which will verify if voted number exists)
  candidate_id = db.Column(db.Integer, db.ForeignKey("candidates.id"), nullable=True)
  blank_vote = db.Column(db.Boolean)
  null_vote = db.Column(db.Boolean)

  electoral_sections = db.relationship("ElectoralSectionModel", back_populates="votes")
  candidates = db.relationship("CandidateModel", back_populates="votes")
  