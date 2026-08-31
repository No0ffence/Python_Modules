class Plant:
    def __init__(self, name: str, height: float, plant_age: int,
                 plant_category: int = 1) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.plant_category = plant_category

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")

    def grow(self) -> None:
        if self.plant_category == 1:
            self.height = round(self.height * 1.01, 2)
        elif self.plant_category == 2:
            self.height = round(self.height * 1.02, 2)
        else:
            self.height = round(self.height * 1.03, 2)

    def age(self) -> None:
        self.plant_age += 1

    def grow_week(self) -> None:
        start_height = self.height
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            self.grow()
            self.age()
            self.show()
        print(f"Growth this week: {round(self.height - start_height, 2)}cm")


def main() -> None:
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    cactus = Plant("Cactus", 15, 50)
    sunflower = Plant("Sunflower", 100, 40)
    tulip = Plant("Tulip", 10, 10)
    potato = Plant("Potato", 35, 18)
    plants = [rose, cactus, sunflower, tulip, potato]
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
