import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")

    print("Now show that not all functions can be reached")
    try:
        alchemy.create_earth()
    except AttributeError as e:
        print(f"Error: {e}")


main()
