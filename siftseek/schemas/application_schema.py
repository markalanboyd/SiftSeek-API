from marshmallow import fields, post_dump
from marshmallow.validate import Length, Range
from marshmallow_enum import EnumField

from siftseek.extensions import ma
from siftseek.models.application import Application
from siftseek.schemas.validators import validate_phone_number


class ApplicationSchema(ma.SQLAlchemyAutoSchema):
    # Foreign Keys
    seeker_id = fields.Integer(validate=Range(min=1))
    # job_posting_id = fields.Integer(validate=Range(min=1))

    # Application Fields
    submitted_at = fields.DateTime()
    status = fields.String(validate=Length(max=250))
    cover_letter = fields.String(validate=Length(max=10_000))

    # Company-Owned Attributes
    reviewed_by = fields.String(validate=Length(max=250))
    interview_date = fields.DateTime()
    rejection_reason = fields.String(validate=Length(max=250))
    notes = fields.String(validate=Length(10_000))

    class Meta:
        model = Application
        load_instance = True
        include_fk = True
        include_relationships = True


application_schema = ApplicationSchema()
applications_schema = ApplicationSchema(many=True)
