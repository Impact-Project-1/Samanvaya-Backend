# Testing Phone Number Validation and Normalisation

This test suite lives in `test/test_phonenumber.py` and uses `pytest`.

## What is covered

The validation tests check the contract of `core.validate.validate_phone_number`:

- It returns the original, unmodified string when the phone number matches the accepted regex.
- It raises `ValueError` when the input has unsupported length, characters, spacing, separators, or country-code shape.
- It intentionally tests the current regex behavior, including cases like `0000000000`, because validation is only a format check and not a real-world number check.

The normalisation tests check the contract of `core.normalise.normalise_phone_number`:

- It asks `geolocator.geocode(address, addressdetails=True)` for region details.
- It converts valid regional numbers into E.164 format, such as `+919876543210`.
- It supports several regions through `phonenumbers`, including India, the US, the UK, and Australia.
- It falls back to India (`IN`) when geocoding returns no location or no country code.
- It wraps parse and validity failures in `ValueError` with the message prefix `Failed to normalise number`.

## Why geopy is mocked

`normalise_phone_number` uses geopy's `Nominatim` geocoder. Tests should be deterministic and should not depend on network access, rate limits, or external geocoder data, so the test fixture patches `core.normalise.geolocator`.

Each normalisation test controls the geocoder response by returning a small mock object with a `raw` dictionary that looks like geopy's location data:

```python
mock_location.raw = {"address": {"country_code": "in"}}
```

This keeps the test focused on the normalisation logic rather than the external geocoding service.

## Test case count

The suite includes more than 15 distinct phone-number cases:

- 9 validation success cases
- 10 validation failure cases
- 6 normalisation success cases
- 2 fallback normalisation cases
- 3 normalisation failure cases
- 1 full validate-to-normalise workflow case

## Running the tests

Run the phone-number tests with:

```bash
python -m pytest test/test_phonenumber.py
```

Run the full configured test suite with:

```bash
python -m pytest
```

The root `.pytest.toml` file configures pytest to discover tests in the `test` directory, use strict config and marker handling, and show useful short summaries.
