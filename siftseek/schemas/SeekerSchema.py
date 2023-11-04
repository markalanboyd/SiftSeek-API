from siftseek.extensions import ma
from siftseek.models.seeker import Seeker


class SeekerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Seeker
        load_instance = True
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "contact_email",
            "work_phone",
            "cell_phone",
            "address",
            "city",
            "resume_url",
            "linkedin_url",
            "portfolio_url",
            "summary",
            "education_level_id",
            "remote_option",
        )
