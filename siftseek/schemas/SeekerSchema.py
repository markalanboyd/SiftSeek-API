from siftseek.extensions import ma
from siftseek.models.seeker import Seeker


# Main Seeker Schema with Nested fields
class SeekerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Seeker


seeker_schema = SeekerSchema()
seekers_schema = SeekerSchema(many=True)
