"""
normalisation functions

normalisation functions should return the normalised value
and must raise an error when the normalisation cannot be conducted
smoothly(just in case clause).

function definition guidelines:
    - normalisation functions shall be prefixed with normalise_
    - use snake cases for function names
    - should mention parameter type in function header
    - docstring describing what the normalisation aims to achieve
    - return type shall be mentioned in function header with ->
    - untested normalisation function shall be marked as #TODO
"""

from geopy.geocoders import Nominatim
import phonenumbers

geolocator = Nominatim(user_agent="Samanvaya")


def normalise_phone_number(phone_number: str, address: str) -> str:  # TODO
    """
    normalise phone numbers based on region to a standard format

    use the geopy to extract and identify region from address,
    provide that regionn code to the phonenumber validation
    function inroder to conduct region specific normalisation
    """

    # extract the region code from address
    location = geolocator.geocode(address, addressdetails=True)
    raw_address = getattr(location, "raw", {}).get("address", {}) if location else {}
    region: str = raw_address.get("country_code", "in").upper() or "IN"

    # normalise the number
    try:
        parsed_number = phonenumbers.parse(phone_number, region)
        if phonenumbers.is_valid_number(parsed_number):
            normalised_number = phonenumbers.format_number(
                parsed_number, phonenumbers.PhoneNumberFormat.E164
            )
        else:
            raise ValueError(f"Phone number invalid for region: {region}")
    except Exception as e:
        raise ValueError(f"Failed to normalise number {phone_number}") from e

    return normalised_number
