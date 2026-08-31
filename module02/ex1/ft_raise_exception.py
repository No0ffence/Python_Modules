def input_temperature(temp_str: str) -> int | None:
    print(f"Input data is '{temp_str}'")
    try:
        temp = int(temp_str)
        if temp < 0:
            print(f"Caught input_temperature error: "
                  f"{temp}°C is too cold for plants (min 0°C)")
            return None
        elif temp > 40:
            print(f"Caught input_temperature error: "
                  f"{temp}°C is too hot for plants (max 40°C)")
            return None
        else:
            return temp
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return None


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    inputs = ["25", "abc", "100", "-50"]
    for i in inputs:
        temp = input_temperature(i)
        if temp:
            print(f"Temperature is now {temp}°C")

    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
