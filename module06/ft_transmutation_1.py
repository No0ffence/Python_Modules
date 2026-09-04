import alchemy.transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(
        f"Testing lead to gold: "
        f"{alchemy.transmutation.recipes.lead_to_gold()}")


main()
