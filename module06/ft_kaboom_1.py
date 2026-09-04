from grimoire import dark_spellbook


def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    ing = 'Earth wind fire'
    print(
        f"Testing record light spell: "
        f"{dark_spellbook('Fantasy', ing)}")


main()
