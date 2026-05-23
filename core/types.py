"""
API wide custom type definitions

pydantic types,
only validations shall be conducted at the type definition level
normalisation, to be conducted at model defintiion level

type definition guidlines
    - use PascalCase for type names
    - document the exact purpose of the type
    - add the adapter of corresponding type to Adapter class (shared instance for validation)
"""

from pydantic import TypeAlias, TypeAdapter, AfterValidator, Annotated

from core.validate import validate_phone_number

# phone number type
# used when the field, requires to receive phone number
# from the user

PhoneNumberString: TypeAlias = Annotated[str, AfterValidator(validate_phone_number)]


# type adapter instances
class Adapters:
    PhoneNumberString = TypeAdapter(PhoneNumberString)


__all__ = ["Adapters", "PhoneNumberString"]
