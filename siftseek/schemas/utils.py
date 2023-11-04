from typing import Any, Set

from marshmallow import post_dump
from marshmallow.validate import Regexp


def partition_data_by_fields(data: dict[str, Any], fields: Set[str]) -> dict:
    """
    Segregates the specified fields from the data into a separate dictionary.

    Args:
        data (dict[str, Any]): The original dictionary containing all fields.
        fields (Set[str]): A set of field names to partition from the original data.

    Returns:
        dict: A dictionary containing only the specified fields.
    """
    return {key: data.pop(key) for key in list(fields) if key in data}


def nest_data(data: dict[str, Any], field_categories_dict: dict[str, set]) -> dict:
    """
    Nests each field category and its fields into a dictionary.

    Args:
        data (dict[str, Any]): The original dictionary containing all fields.
        field_categories (dict[str, set]): A dictionary of sets of field names to partition from the original data.

    Returns:
        dict: A dataset nested by categories.
    """
    nested_data = {}
    for category, fields in field_categories_dict.items():
        nested_data[category] = partition_data_by_fields(data, fields)
    return nested_data


def validate_phone_number():
    return Regexp(
        r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$",
        error="Invalid phone number format.",
    )
