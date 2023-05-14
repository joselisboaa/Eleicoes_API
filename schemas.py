from marshmallow import Schema, fields

class CitySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    state_abbreviation = fields.Str(required=True)
    group_of_councilors = fields.Int(required=True)

class PlainElectoralZoneSchema(Schema):
    id = fields.Int(dump_only=True)
    zone = fields.Str(required=True)

class PlainElectoralSectionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainPartySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    abbreviation = fields.Str(required=True)

class PartySchema(PlainPartySchema):
    alliance_party_id = fields.Int(load_only=True)
    alliance_party = fields.Nested(PlainPartySchema(), dump_only=True)

class PlainCandidateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    number = fields.Int(required=True)

class PositionSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainVoteSchema(Schema):
    id = fields.Int(dump_only=True)
    blank_vote = fields.Int()
    null_vote = fields.Int()


class VoteSchema(PlainVoteSchema):
    section_id = fields.Int(required=True, load_only=True)
    candidate_id = fields.Int(required=True, load_only=True)
    section = fields.Nested(PlainElectoralSectionSchema(), dump_only=True)
    candidate = fields.Nested(PlainCandidateSchema(), dump_only=True)


class CandidateSchema(PlainCandidateSchema):
    position_id = fields.Int(required=True, load_only=True)
    party_id = fields.Int(required=True, load_only=True)

    position = fields.Nested(PositionSchema(), dump_only=True)
    party = fields.Nested(PlainPartySchema(), dump_only=True)
    
class AlliancePartySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class ElectoralSectionSchema(PlainElectoralSectionSchema):
    zone_id = fields.Int(required=True, load_only=True)
    zone = fields.Nested(PlainElectoralSectionSchema(), dump_only=True)

class ElectoralZoneSchema(PlainElectoralZoneSchema):
    city_id = fields.Int(required=True, load_only=True)
    city = fields.Nested(PlainElectoralZoneSchema(), dump_only=True)
