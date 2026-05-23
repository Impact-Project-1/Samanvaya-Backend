import pytest
from unittest.mock import MagicMock, patch

from core.normalise import normalise_phone_number
from core.validate import validate_phone_number

# Note: In a production setup, ensure your geolocator has a custom user_agent [5]
# from your_module import validate_phone_number, normalise_phone_number


# --- Mocking Setup ---
@pytest.fixture
def mock_geolocator():
    """Mocks the geopy geolocator to avoid network calls [2, 3]."""
    with patch("your_module.geolocator") as mocked_geolocator:
        yield mocked_geolocator


# --- Tests for validate_phone_number ---


@pytest.mark.parametrize(
    "phone",
    [
        "9876543210",  # Standard 10-digit
        "+91 9876543210",  # International with 2-digit code
        "+123 9876543210",  # International with 3-digit code
        "12345 67890",  # Split 5-5 format
    ],
)
def test_validate_phone_number_success(phone):
    """Tests that valid formats pass the regex [History]."""
    assert validate_phone_number(phone) == phone


@pytest.mark.parametrize(
    "phone",
    [
        "12345",  # Too short
        "abcdefghij",  # Non-numeric
        "+9 9876543210",  # International code too short
        "987654321011",  # Too long
    ],
)
def test_validate_phone_number_failure(phone):
    """Tests that invalid formats raise ValueError [History]."""
    with pytest.raises(
        ValueError, match="Phone number doesnt not follow standard format"
    ):
        validate_phone_number(phone)


# --- Tests for normalise_phone_number ---


def test_normalise_phone_number_india_success(mock_geolocator):
    """Tests normalisation for an Indian address [History]."""
    # Mock geopy Location object and .raw dictionary [6-8]
    mock_location = MagicMock()
    mock_location.raw = {"address": {"country_code": "in"}}
    mock_geolocator.geocode.return_value = mock_location

    result = normalise_phone_number("9876543210", "123 MG Road, Mumbai")
    assert result == "+919876543210"  # E.164 format [History]


def test_normalise_phone_number_us_success(mock_geolocator):
    """Tests normalisation for a US address [History]."""
    mock_location = MagicMock()
    mock_location.raw = {"address": {"country_code": "us"}}
    mock_geolocator.geocode.return_value = mock_location

    # A 10-digit US number
    result = normalise_phone_number(
        "2025550123", "1600 Pennsylvania Avenue, Washington DC"
    )
    assert result == "+12025550123"


def test_normalise_phone_number_invalid_address(mock_geolocator):
    """Tests fallback to 'IN' when geopy returns no results [6]."""
    # Geocoders return None when no results are found [6]
    mock_geolocator.geocode.return_value = None

    # Should fallback to 'IN' as per your code logic
    result = normalise_phone_number("9876543210", "Nonexistent Place")
    assert result == "+919876543210"


def test_normalise_phone_number_invalid_for_region(mock_geolocator):
    """Tests failure when number passes regex but is invalid for the region [History]."""
    mock_location = MagicMock()
    mock_location.raw = {"address": {"country_code": "us"}}  # US Region
    mock_geolocator.geocode.return_value = mock_location

    # This number passes your regex but is not a valid US number
    with pytest.raises(ValueError, match="Failed to normalise number"):
        normalise_phone_number("9876543210", "New York, USA")


# --- Integration Test: Full Workflow ---


def test_full_phone_workflow(mock_geolocator):
    """Tests the combined flow: validate -> normalise [History]."""
    mock_location = MagicMock()
    mock_location.raw = {"address": {"country_code": "in"}}
    mock_geolocator.geocode.return_value = mock_location

    raw_input = " 9876543210 "
    address = "Bangalore, India"

    # 1. Basic string cleanup
    cleaned_input = raw_input.strip()

    # 2. Validation
    validated = validate_phone_number(cleaned_input)

    # 3. Normalisation
    final = normalise_phone_number(validated, address)

    assert final == "+919876543210"
