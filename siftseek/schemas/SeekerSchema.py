from marshmallow import fields, validate, post_dump

from siftseek.extensions import ma
from siftseek.models.seeker import Seeker


class PersonalInfoSchema(ma.Schema):
    username = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    contact_email = fields.Email(required=True)
    work_phone = fields.Str()
    work_phone_ext = fields.Str()
    cellphone = fields.Str()
    address = fields.Str()
    city = fields.Str()


class SeekerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Seeker
        load_instance = True
        include_fk = True
        include_relationships = True

    metadata_fields = {"id", "_created_at", "modified_at", "deleted_at"}
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

    def __parse_fields(self, data, fields) -> dict:
        return {key: data.pop(key) for key in list(fields) if key in data}

    @post_dump(pass_many=False)
    def nest_json(self, data, **kwargs):
        field_categories = {
            "metadata": self.metadata_fields,
            "personal_info": self.personal_info_fields,
            "urls": self.url_fields,
            "resume_info": self.resume_info_fields,
        }

        # Initialize the nested structure
        nested_data = {}
        for category, fields in field_categories.items():
            nested_data[category] = self.__parse_fields(data, fields)

        # Update the data dictionary with the nested data
        data.update(nested_data)
        return data


# Create an instance of the SeekerSchema
seeker_schema = SeekerSchema()

seekers_schema = SeekerSchema(many=True)
