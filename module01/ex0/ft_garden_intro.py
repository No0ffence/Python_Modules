class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def print_info(self) -> None:
        print(f"Plant: {self.name}")
        print(f"Height: {self.height}cm")
        print(f"Age: {self.age}days")


def main() -> None:
    print("=== Welcome to My Garden ===")
    rose = Plant("Rose", 25, 30)
    rose.print_info()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
