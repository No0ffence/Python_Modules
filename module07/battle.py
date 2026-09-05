from ex0 import FlameFactory, AquaFactory, CreatureFactory


def create_characters(factory: CreatureFactory) -> None:
    print("\nTesting factory")
    try:
        base_character = factory.create_base()
        evolved_character = factory.create_evolved()
        print(base_character.describe())
        print(base_character.attack())
        print(evolved_character.describe())
        print(evolved_character.attack())
    except Exception as e:
        print(f"You cant create that type of character {e}")


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("\nTesting battle")
    try:
        first_char = factory1.create_base()
        second_char = factory2.create_base()
        print(f"{first_char.describe()}\n vs. \n{second_char.describe()}")
        print("fight!")
        print(first_char.attack())
        print(second_char.attack())
    except Exception as e:
        print(f"You cant create that type of character {e}")


def main() -> None:
    flamelingFactoty = FlameFactory()
    aquabublingFactoty = AquaFactory()
    create_characters(flamelingFactoty)
    create_characters(aquabublingFactoty)
    battle(flamelingFactoty, aquabublingFactoty)


if __name__ == "__main__":
    main()
