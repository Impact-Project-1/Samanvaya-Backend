"""
validator functions shall be handled here

defined functions should only return the same un-normalised value
or raise an exception in case of failure to validate, depending on the
validation logic and context.

function definition guidelines:
   - validation functions shall be prefixed with 'validate_'
   - use snake cases for function name
   - should mention the parameter type in the function header
   - docstring for each validating function, describing what all the validation does
   - return type shall be marked with ->
   - validator functions that are either untested/undergoing testing and improvement shall be marked #TODO
"""

import re


def validate_phone_number(phone_number: str) -> str:  # TODO
    """
    validate using basic constraints
    """

    if not re.fullmatch(r"^(?:\+\d{2,3}\s)?(?:\d{10}|\d{5} \d{5})$", phone_number):
        raise ValueError("Phone number doesnt not follow standard format")
    return phone_number
