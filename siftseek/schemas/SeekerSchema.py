from marshmallow import fields, validate, post_dump

from siftseek.extensions import ma
from siftseek.models.seeker import Seeker
from siftseek.schemas.utils import nest_data


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
