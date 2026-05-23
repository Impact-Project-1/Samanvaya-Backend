import pytest
from unittest.mock import MagicMock, patch

from core.normalise import normalise_phone_number
from core.validate import validate_phone_number


# --- Mocking Setup ---
@pytest.fixture
def mock_geolocator():
    """Mock geopy so tests never make network calls."""
    with patch("core.normalise.geolocator") as mocked_geolocator:
        yield mocked_geolocator


def set_country(mock_geolocator, country_code):
    mock_location = MagicMock()
    mock_location.raw = {"address": {"country_code": country_code}}
    mock_geolocator.geocode.return_value = mock_location


# --- Tests for validate_phone_number ---


@pytest.mark.parametrize(
    "phone",
    [
        "9876543210",  # Standard 10-digit
        "+91 9876543210",  # International with 2-digit code
        "+123 9876543210",  # International with 3-digit code
        "12345 67890",  # Split 5-5 format
        "+977 9841234567",  # International with 3-digit Nepal code
        "0000000000",  # Regex allows any 10 digits
        "+44 0207946005",  # Regex allows leading zero in local part
        "+91 98765 43210",  # Country code with split 5-5 local format
        "+912 98765 43210",  # Three-digit country code with split local format
    ],
)
def test_validate_phone_number_success(phone):
    assert validate_phone_number(phone) == phone


@pytest.mark.parametrize(
    "phone",
    [
        "12345",  # Too short
        "abcdefghij",  # Non-numeric
        "+9 9876543210",  # International code too short
        "987654321011",  # Too long
        "98765-43210",  # Separators other than the single allowed space fail
        " 9876543210",  # Leading whitespace is not accepted
        "9876543210 ",  # Trailing whitespace is not accepted
        "+1234 9876543210",  # Country code too long
        "+91 987654321",  # Local number too short after country code
        "9876 543210",  # Split format must be 5-5 digits
    ],
)
def test_validate_phone_number_failure(phone):
    with pytest.raises(
        ValueError, match="Phone number doesnt not follow standard format"
    ):
        validate_phone_number(phone)


# --- Tests for normalise_phone_number ---


@pytest.mark.parametrize(
    ("phone", "country_code", "expected"),
    [
        ("9876543210", "in", "+919876543210"),
        ("98765 43210", "in", "+919876543210"),
        ("+91 9876543210", "in", "+919876543210"),
        ("2025550123", "us", "+12025550123"),
        ("02079460056", "gb", "+442079460056"),
        ("0412345678", "au", "+61412345678"),
    ],
)
def test_normalise_phone_number_success(mock_geolocator, phone, country_code, expected):
    set_country(mock_geolocator, country_code)

    result = normalise_phone_number(phone, "region-specific address")

    assert result == expected
    mock_geolocator.geocode.assert_called_once_with(
        "region-specific address", addressdetails=True
    )


def test_normalise_phone_number_invalid_address(mock_geolocator):
    mock_geolocator.geocode.return_value = None

    result = normalise_phone_number("9876543210", "Nonexistent Place")

    assert result == "+919876543210"


def test_normalise_phone_number_missing_country_code_falls_back_to_india(
    mock_geolocator,
):
    mock_location = MagicMock()
    mock_location.raw = {"address": {}}
    mock_geolocator.geocode.return_value = mock_location

    result = normalise_phone_number("9876543210", "Address without country")

    assert result == "+919876543210"


@pytest.mark.parametrize(
    ("phone", "country_code"),
    [
        ("9876543210", "us"),  # Valid-looking Indian number, invalid for US
        ("12345", "in"),  # Too short for India
        ("abcdefghij", "in"),  # Cannot be parsed as a phone number
    ],
)
def test_normalise_phone_number_failure(mock_geolocator, phone, country_code):
    set_country(mock_geolocator, country_code)

    with pytest.raises(ValueError, match="Failed to normalise number"):
        normalise_phone_number(phone, "region-specific address")


# --- Integration Test: Full Workflow ---


def test_full_phone_workflow(mock_geolocator):
    set_country(mock_geolocator, "in")

    raw_input = " 9876543210 "
    address = "Bangalore, India"

    # 1. Basic string cleanup
    cleaned_input = raw_input.strip()

    # 2. Validation
    validated = validate_phone_number(cleaned_input)

    # 3. Normalisation
    final = normalise_phone_number(validated, address)

    assert final == "+919876543210"
