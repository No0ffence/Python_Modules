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


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, plant_category: int,
                 color: str) -> None:
        super().__init__(name, height, age, plant_category)
        self.color = color
        self.is_bloom = 0

    def bloom(self) -> None:
        self.is_bloom = 1
        print("[asking the rose to bloom]")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if not self.is_bloom:
            print(f"{self._name} has not bloomed yet")
        else:
            print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, plant_category: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age, plant_category)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print("[asking the tree to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, plant_category: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age, plant_category)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self, times: int = 1) -> None:
        print(f"[make {self._name} grow and age for {times} days]")
        for i in range(times):
            super().age()
            super().grow()
            self.nutritional_value += 1

    def age(self, times: int = 1) -> None:
        print(f"[make {self._name} grow and age for {times} days]")
        for i in range(times):
            super().age()
            super().grow()
            self.nutritional_value += 1


def main() -> None:
    print("=== Garden Plant Types ===")

    print("\n=== Flower")
    rose = Flower("Rose", 25, 30, 2, "red")
    rose.show()
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 100, 40, 1, 15)
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    potato = Vegetable("Potato", 35,
                       18, 3, "summer")
    potato.show()
    potato.age(20)
    potato.show()


if __name__ == "__main__":
    main()
