from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    """Common configuration, inherited by all subsequent
    configuration classes"""

    model_config = ConfigDict(
        user_enum_values=True,
    )


class RestrictedBase(Base):
    """inherit when the model needs to restrict extra fields"""

    model_config = ConfigDict(
        extra="fobid",
    )


__all__ = ["RestrictedBase"]
