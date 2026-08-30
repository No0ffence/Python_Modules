from alchemy.potions import healing_potion, strength_potion


def main():
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {healing_potion()}")
    print(f"Testing healing_potion: {strength_potion()}")


main()
