"""
The validators.py file in siftseek.schemas module provides custom validator
functions meant for use with marshmallow schemas.
"""

import phonenumbers

from marshmallow import ValidationError


def validate_phone_number(phone_number: str) -> None:
    """
    Throws an error if the phone number does not conform to formatting
    recognized by the phonenumbers package.

    Args:
        phone_number (str): Phone number to be validated.

    Raises:
        ValidationError: Throws an error if phone number format not recognized.
    """
    error_msg = "Invalid phone number format."
    try:
        phone_number_obj = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_possible_number(phone_number_obj):
            raise ValidationError(error_msg)
    except phonenumbers.NumberParseException:
        raise ValidationError(error_msg)
