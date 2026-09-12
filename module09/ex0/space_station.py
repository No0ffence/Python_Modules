from pydantic import BaseModel, Field
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=1, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main():
    station1 = SpaceStation(station_id="ISS001",
                            name="International Space Station",
                            crew_size=6,
                            power_level=85.5,
                            oxygen_level=92.3,
                            last_maintenance=datetime.now())


if __name__ == "__main__":
    main()
