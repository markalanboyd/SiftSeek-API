from marshmallow import fields
from marshmallow.validate import Length, Email, URL

from siftseek.extensions import ma
from siftseek.models.seeker import Seeker
from siftseek.schemas.validators import validate_phone_number


class SeekerSchema(ma.SQLAlchemySchema):
    """
    Schema for serializing and deserializing instances of the Seeker model.

    This schema is specifically designed for handling data transformation to and
    from the SeekerSchema model, facilitating the process of converting JSON
    data into model instances and vice versa.

    It is built using marshmallow's SQLAlchemySchema, which provides customized
    serialization and deserialization capabilities.
    """

    username = fields.String(validate=Length(min=1, max=20))
    first_name = fields.String(validate=Length(min=1, max=255))
    last_name = fields.String(validate=Length(min=1, max=255))
    contact_email = fields.Email(validate=Email())
    work_phone = fields.String(validate=validate_phone_number)
    work_phone_ext = fields.String(validate=Length(min=1, max=5))
    cellphone = fields.String(validate=validate_phone_number)
    address = fields.String(validate=Length(min=1, max=255))
    city = fields.String(validate=Length(min=1, max=255))
    profile_pic_url = fields.Url(validate=URL())
    resume_url = fields.Url(validate=URL())
    linkedin_url = fields.Url(validate=URL())
    portfolio_url = fields.Url(validate=URL())
    summary = fields.String(validate=Length(max=10_000))
    education_level = fields.String(validate=Length(max=250))
    remote_option = fields.Boolean()

    class Meta:
        model = Seeker
        load_instance = True
        include_fk = True
        include_relationships = True


seeker_schema = SeekerSchema()
seekers_schema = SeekerSchema(many=True)
