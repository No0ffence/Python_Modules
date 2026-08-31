class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caught GardenError: {self.message}"


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error"):
        super().__init__(message)

    def __str__(self) -> str:
        return f"Caught PlantError: {self.message}"


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f" Invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Opening watering system")
    plants = ["Tomato", "Lettuce", "Carrots", "tomato"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(e)
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")


def main() -> None:
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
