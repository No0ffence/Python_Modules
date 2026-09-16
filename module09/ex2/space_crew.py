from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, model_validator


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        if Rank.captain not in self.crew or Rank.commander not in self.crew:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced = len([i for i in self.crew if i.years_experience > 5])
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) "
                    "need 50% experienced crew (5+ years)")
        for memb in self.crew:
            if not memb.is_active:
                raise ValueError("All crew members must be active")
        return self


def main():
    print("""
Space Mission Crew Validation
=========================================""")

    print("Valid mission created:")

    memb1 = CrewMember(
        member_id="lox",
        name="Navonial",
        rank=Rank.cadet,
        age=19,
        specialization="Glavnya po prisutstviu",
        years_experience=1,
        is_active=True
    )
    memb2 = CrewMember(
        member_id="Popusk",
        name="Ivan",
        rank=Rank.captain,
        age=33,
        specialization="Smotriashij",
        years_experience=7,
        is_active=True
    )
    memb3 = CrewMember(
        member_id="Korzura",
        name="Dima",
        rank=Rank.lieutenant,
        age=29,
        specialization="Glavnyj po hiptrastam",
        years_experience=5,
        is_active=True
    )
    crew = [memb1, memb2, memb3]

    good_mission = SpaceMission(
        mission_id="Lukashenko pidor",
        mission_name="Zahvat usotago",
        destination="Residence of Lukashenko",
        launch_date=datetime.now(),
        duration_days=25,
        crew=crew,
        budget_millions=10000
    )
    # todo
    # good_mission.show()


if __name__ == "__main__":
    main()
