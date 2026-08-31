def input_temperature(temp_str: str) -> int | None:
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
        return temp
    except ValueError:
        print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: '{temp_str}'")
        return None


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    inputs = ["25", "abc"]
    for i in inputs:
        temp = input_temperature(i)
        if temp:
            print(f"Temperature is now {temp}°C")

    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    test_temperature()
