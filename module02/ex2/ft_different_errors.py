def garden_operations(operation_number: int) -> int | None:
    value = "abc"
    num = 10
    file_path: str = '/non/existent/file'
    try:
        if operation_number == 1:
            num / 0
            return num
        elif operation_number == 0:
            num = int(value)
            return num
        elif operation_number == 2:
            open(file_path)
            return None
        elif operation_number == 3:
            value + 10
            return num
        else:
            print("Operation completed successfully")
            return operation_number
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
        return None
    except ValueError as e:
        print(f"Caught ValueError: {e} ")
        return None
    except FileNotFoundError as e:
        print(
            f"Caught FileNotFoundError: {e} ")
        return None
    except TypeError as e:
        print(
            f"Caught TypeError: {e}")
        return None


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    garden_operations(0)
    print("Testing operation 1...")
    garden_operations(1)
    print("Testing operation 2...")
    garden_operations(2)
    print("Testing operation 3...")
    garden_operations(3)
    print("Testing operation 4...")
    garden_operations(4)
    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
