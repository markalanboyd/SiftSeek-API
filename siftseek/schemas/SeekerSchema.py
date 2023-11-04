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

    # Define the fields that will be nested inside personal_info
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

    # We define a method to reformat the data to include the personal_info nesting
    @post_dump(pass_many=False)
    def nest_personal_info(self, data, many, **kwargs):
        personal_info = {
            key: data.pop(key) for key in self.personal_info_fields if key in data
        }
        data["personal_info"] = personal_info
        return data


seeker_schema = SeekerSchema()
seekers_schema = SeekerSchema(many=True)
