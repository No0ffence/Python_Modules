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
        self.stats = self.Statistic(name)

    def show(self) -> None:
        print(
            f"{self._name}: {self._height:.1f}cm, {self._plant_age} days old")
        self.stats.set_show_times()

    def grow(self) -> None:
        if self._plant_category == 1:
            self._height = round(self._height * 1.01, 2)
        elif self._plant_category == 2:
            self._height = round(self._height * 1.02, 2)
        else:
            self._height = round(self._height * 1.03, 2)
        self.stats.set_grow_times()

    def age(self) -> None:
        self._plant_age += 1
        self.stats.set_age_times()

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

    @staticmethod
    def check_age(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anon(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    class Statistic:
        def __init__(self, name: str):
            self._name = name
            self._n_of_grow: int = 0
            self._n_of_age: int = 0
            self._n_of_show: int = 0

        def display(self) -> None:
            print(f"[statistics for {self._name}]")
            print(
                f"Stats: {self._n_of_grow} grow, "
                f"{self._n_of_age} age, {self._n_of_show} show")

        def set_grow_times(self) -> None:
            self._n_of_grow += 1

        def set_age_times(self) -> None:
            self._n_of_age += 1

        def set_show_times(self) -> None:
            self._n_of_show += 1


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
        self.stats: Tree.Statistic = self.Statistic(name)

    def produce_shade(self) -> None:
        print("[asking the tree to produce shade]")
        print(
            f"Tree {self._name} now produces a shade "
            f"of {self._height:.1f}cm long "
            f"and {self.trunk_diameter:.1f}cm wide.")
        self.stats.set_shade_times()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    class Statistic(Plant.Statistic):
        def __init__(self, name: str):
            super().__init__(name)
            self._n_of_shade: int = 0

        def display(self) -> None:
            super().display()
            print(f"{self._n_of_shade} shade")

        def set_shade_times(self) -> None:
            self._n_of_shade += 1


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


class Seed(Flower):

    def __init__(self, name: str, height: int, age: int, plant_category: int,
                 color: str):
        super().__init__(name, height, age, plant_category, color)
        self.seeds = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds += 42


def show_stats(plant: Plant) -> None:
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    days: int = 30
    print(f"Is {days} days more than a year? -> {Plant.check_age(days)}")
    days = 400
    print(f"Is {days} days more than a year? -> {Plant.check_age(days)}")

    print("\n=== Flower")
    rose = Flower("Rose", 25, 30, 2, "red")
    rose.show()
    show_stats(rose)
    rose.bloom()
    rose.grow()
    show_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 100, 40, 1, 15)
    oak.show()
    show_stats(oak)
    oak.produce_shade()
    show_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower",
                     110, 65, 1, "yellow")
    sunflower.show()
    sunflower.bloom()
    sunflower.show()

    print("\n=== Anonymous")
    anon = Plant.create_anon()
    anon.show()
    show_stats(anon)


if __name__ == "__main__":
    main()
