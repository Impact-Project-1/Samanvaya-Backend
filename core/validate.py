"""Pydantic validator support"""

def validate_phone_number(cls, v:str) -> str:
        if not re.match(r"^\+[1-9]\d{1,14}$", v):
            raise ValueError("Phone number format must be in valid E.164 format, eg: +1234567890")
        # TODO: normalise
        return v

def validate_password_strength(cls, v:str) -> str:
        if not all([re.search(r"[A-Z]", v), re.search(r"[a-z]", v), re.search(r"[0-9]", v)]):
            raise ValueError("Password must contain uppercase. lowercase and numeric characters")
        return v