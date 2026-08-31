class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caught GardenError: {self.message}"


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)

    def __str__(self) -> str:
        return f"Caught PlantError: {self.message}"


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)

    def __str__(self) -> str:
        return f"Caught WaterError: {self.message}"


def check_water_satus(water_in_tank: int) -> None:
    if water_in_tank < 10:
        raise WaterError("Not enough water in the tank!")


def check_plant_satus(days_after_watering: int) -> None:
    if days_after_watering > 3:
        raise PlantError("The tomato plant is wilting!")


def test_errors(water_in_tank: int, days_after_watering: int) -> None:
    print("\nTesting PlantError...")
    try:
        check_plant_satus(days_after_watering)
    except PlantError as e:
        print(e)

    print("\nTesting WaterError...")
    try:
        check_water_satus(water_in_tank)
    except WaterError as e:
        print(e)

    print("\nTesting catching all garden errors...")
    try:
        check_plant_satus(days_after_watering)
    except GardenError as e:
        print(e)
    try:
        check_water_satus(water_in_tank)
    except GardenError as e:
        print(e)


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    test_errors(0, 5)
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
