from enum import Enum

from pydantic import BaseModel, Field, model_validator
from datetime import datetime


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    def show(self) -> None:
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength} / 10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witnesses: {self.witness_count}")
        if self.message_received:
            print(f"Message: {self.message_received}")
        else:
            print("Message: not received")

    @model_validator(mode="after")
    def validate_model(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if not self.is_verified:
            raise ValueError('Physical contact reports must be verified')
        if self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                'Strong signals (> 7.0) should include received messages')
        return self


def main() -> None:
    alien1 = AlienContact(contact_id="AC_2024_001",
                          contact_type=ContactType.radio,
                          location="Area 51, Nevada",
                          signal_strength=8.5,
                          duration_minutes=45,
                          witness_count=5,
                          timestamp=datetime.now(),
                          message_received='Greetings from Zeta Reticuli',
                          is_verified=True)

    print("""
Alien Contact Log Validation
======================================""")
    print("Valid contact report:")
    alien1.show()

    print("""
========================================
Expected validation error:""")
    try:
        alien2 = AlienContact(contact_id="AC_2024_001",
                              contact_type=ContactType.radio,
                              location="Area 51, Nevada",
                              signal_strength=8.5,
                              duration_minutes=45,
                              witness_count=2,
                              timestamp=datetime.now(),
                              message_received='Greetings from Zeta Reticuli',
                              is_verified=True)
        alien2.show()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
