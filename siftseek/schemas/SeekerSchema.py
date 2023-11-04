from marshmallow import fields, post_dump
from marshmallow.validate import Length, Email, URL, Range

from siftseek.extensions import ma
from siftseek.models.seeker import Seeker
from siftseek.schemas.utils import nest_data, validate_phone_number


class SeekerSchema(ma.SQLAlchemyAutoSchema):
    # Validators
    length_error = "Length must be between {min} and {max} characters."
    length_255_validator = fields.String(
        validate=Length(min=1, max=255, error=length_error)
    )
    email_validator = fields.Email(validate=Email(error="Invalid email address."))
    phone_number_validator = fields.String(validate=validate_phone_number())
    phone_extension_validator = fields.Integer(
        validate=Length(min=1, max=5), error=length_error
    )
    url_validator = fields.Url(validate=URL(error="Invalid URL."))
    id_validator = fields.Integer(
        validate=Range(min=1, error="Value must be 1 or greater.")
    )
    boolean_validator = fields.Boolean(error="Invalid input for boolean field.")

    username = fields.String(validate=Length(min=1, max=20, error=length_error))
    first_name = length_255_validator
    last_name = length_255_validator
    contact_email = email_validator
    work_phone = phone_number_validator
    work_phone_ext = phone_extension_validator
    cellphone = phone_number_validator
    address = length_255_validator
    city = length_255_validator
    profile_pic_url = url_validator
    resume_url = url_validator
    linkedin_url = url_validator
    portfolio_url = url_validator
    summary = fields.String(validate=Length(min=1, max=10_000, error=length_error))
    education_level_id = id_validator
    remote_option = boolean_validator

    class Meta:
        model = Seeker
        load_instance = True
        include_fk = True
        include_relationships = True

    # Define schema for categories of fields
    metadata_fields = {
        "id",
        "_created_at",
        "modified_at",
        "marked_for_deletion",
        "deleted_at",
    }
    personal_info_fields = {
        "username",
        "first_name",
        "last_name",
        "contact_email",
        "work_phone",
        "work_phone_ext",
        "cellphone",
        "address",
        "city",
    }
    url_fields = {"profile_pic_url", "resume_url", "linkedin_url", "portfolio_url"}
    resume_info_fields = {"summary", "education_level_id", "remote_option"}

    field_categories_dict = {
        "metadata": metadata_fields,
        "personal_info": personal_info_fields,
        "urls": url_fields,
        "resume_info": resume_info_fields,
    }

    @post_dump(pass_many=False)
    def nest_seeker_data(self, data, many):
        nested_data = nest_data(data, self.field_categories_dict)
        data.update(nested_data)
        return data


# Create an instance of the SeekerSchema
seeker_schema = SeekerSchema()

seekers_schema = SeekerSchema(many=True)
