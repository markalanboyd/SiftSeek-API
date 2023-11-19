from marshmallow import fields
from marshmallow.validate import Length, Range

from siftseek.extensions import ma
from siftseek.models.job_application import JobApplication


class JobApplicationSchema(ma.SQLAlchemySchema):
    """
    Schema for serializing and deserializing instances of the JobApplication model.

    This schema is specifically designed for handling data transformation to and
    from the JobApplication model, facilitating the process of converting JSON
    data into model instances and vice versa.

    It is built using marshmallow's SQLAlchemySchema, which provides customized
    serialization and deserialization capabilities.
    """

    # Foreign Keys
    seeker_id = fields.Integer(validate=Range(min=1))
    # Following line commented out at the moment since this model does not yet exist
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
        model = JobApplication
        load_instance = True
        include_fk = True
        include_relationships = True


application_schema = JobApplicationSchema()
applications_schema = JobApplicationSchema(many=True)
