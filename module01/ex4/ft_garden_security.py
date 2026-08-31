class Plant:
    def __init__(self, name: str, height: float, plant_age: int,
                 plant_category: int = 1) -> None:
        if height < 0:
            print("Invalid height")
            height = 0
        if plant_age < 0:
            print("Invalid age")
            plant_age = 0
        self._name = name
        self._height = height
        self._plant_age = plant_age
        self._plant_category = plant_category

    def show(self) -> None:
        print(
            f"{self._name}: {self._height:.1f}cm, {self._plant_age} days old")

    def grow(self) -> None:
        if self._plant_category == 1:
            self._height = round(self._height * 1.01, 2)
        elif self._plant_category == 2:
            self._height = round(self._height * 1.02, 2)
        else:
            self._height = round(self._height * 1.03, 2)

    def age(self) -> None:
        self._plant_age += 1

    def grow_week(self) -> None:
        start_height = self._height
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            self.grow()
            self.age()
            self.show()
        print(f"Growth this week: {round(self._height - start_height, 2)}cm")

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated:  {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def set_age(self, plant_age: int) -> None:
        if plant_age >= 0:
            self._plant_age = plant_age
            print(f"Age updated:  {self._plant_age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self._plant_age


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 30)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(20)
    rose.set_age(10)
    rose.set_height(-1)
    rose.set_age(-10)
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
