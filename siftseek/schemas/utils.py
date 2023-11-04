from typing import Dict, Any, Set

from marshmallow import post_dump


def partition_data_by_fields(data: Dict[str, Any], fields: Set[str]) -> dict:
    """
    Segregates the specified fields from the data into a separate dictionary.

    Args:
        data (Dict[str, Any]): The original dictionary containing all fields.
        fields (Set[str]): A set of field names to partition from the original data.

    Returns:
        dict: A dictionary containing only the specified fields.
    """
    return {key: data.pop(key) for key in list(fields) if key in data}


def nest_data(data: Dict[str, Any], field_categories_dict: Dict[str, Set]) -> dict:
    """
    Nests each field category and its fields into a dictionary.

    Args:
        data (Dict[str, Any]): The original dictionary containing all fields.
        field_categories (Dict[str, Set]): A dictionary of sets of field names to partition from the original data.

    Returns:
        dict: _description_
    """
    nested_data = {}
    for category, fields in field_categories_dict.items():
        nested_data[category] = partition_data_by_fields(data, fields)
    return nested_data
