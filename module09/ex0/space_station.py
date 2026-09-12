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

    def show(self):
        print("Valid station created:")
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level} %")
        print(f"Oxygen: {self.oxygen_level} %")
        if self.is_operational:
            print("Status: Operational")
        else:
            print("Status: Not operational")


def main():
    station1 = SpaceStation(station_id="ISS001",
                            name="International Space Station",
                            crew_size=6,
                            power_level=85.5,
                            oxygen_level=92.3,
                            last_maintenance=datetime.now())

    print("""
Space Station Data Validation
========================================""")
    station1.show()

    print("""
========================================
Expected validation error:""")
    try:
        station2 = SpaceStation(station_id="ISS001455654546",
                                name="International Space Station",
                                crew_size=6,
                                power_level=85.5,
                                oxygen_level=92.3,
                                last_maintenance=datetime.now())
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
