def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    ing = 'Earth wind fire'

    try:
        from grimoire import dark_spellbook
        print(
            f"Testing record light spell: "
            f"{dark_spellbook.dark_spell_record('Fantasy', ing)}")
    except ImportError as e:
        print(e)


main()
