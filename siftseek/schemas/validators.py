from marshmallow import ValidationError

import phonenumbers


def validate_phone_number(phone_number: str) -> None:
    try:
        phone_number_obj = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_possible_number(phone_number_obj):
            raise ValidationError("Invalid phone number format.")
    except phonenumbers.NumberParseException:
        raise ValidationError("Invalid phone number format.")
