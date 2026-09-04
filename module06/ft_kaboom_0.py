import grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    ing = 'Earth wind fire'
    print(
        f"Testing record light spell: "
        f"{grimoire.light_spell_record('Fantasy', ing)}")


main()
