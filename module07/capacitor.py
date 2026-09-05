from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    print("\nTesting Creature with healing capability")
    healing_factory = HealingCreatureFactory()
    try:
        print("base:")
        base_heal_creature = healing_factory.create_base()
        print(base_heal_creature.describe())
        print(base_heal_creature.attack())
        print(base_heal_creature.heal())
        print("evolved:")
        evolved_heal_creature = healing_factory.create_evolved()
        print(evolved_heal_creature.describe())
        print(evolved_heal_creature.attack())
        print(evolved_heal_creature.heal("itself and others"))
    except Exception as e:
        print(f"Error {e}")


def test_transform() -> None:
    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    try:
        print("base:")
        base_heal_creature = transform_factory.create_base()
        print(base_heal_creature.describe())
        print(base_heal_creature.attack())
        print(base_heal_creature.transform())
        print(base_heal_creature.attack())
        print(base_heal_creature.revert())
        print("evolved:")
        evolved_heal_creature = transform_factory.create_evolved()
        print(evolved_heal_creature.describe())
        print(evolved_heal_creature.attack())
        print(evolved_heal_creature.transform())
        print(evolved_heal_creature.attack())
        print(evolved_heal_creature.revert())
    except Exception as e:
        print(f"Error {e}")


def main() -> None:
    test_healing()
    test_transform()


if __name__ == "__main__":
    main()
