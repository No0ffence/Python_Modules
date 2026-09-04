from alchemy import create_air


def main() -> None:
    print("=== Alembic 5 ===")
    print(
        "Accessing the alchemy module using 'from alchemy import ...'")
    print(f"Testing create_air: {create_air()}")


main()
