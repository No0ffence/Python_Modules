import sys


def transform_data(f_name: str) -> None:
    new_f = None
    f = None
    try:
        print("Transform data: \n___\n")
        f = open(f_name, "r")
        lines = f.read().split("\n")
        updated_lines = []
        for line in lines:
            new_line = line + '#'
            updated_lines.append(new_line)
            print(new_line)
        print("\n___\n")
        s_file = input("Enter new file name (or empty):")
        if s_file == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{s_file}'")
            new_f = open(s_file, "w")
            for line in updated_lines:
                new_f.write(line + '\n')
            print(f"Data saved in file '{s_file}'.")
    except OSError as e:
        print(f"Error opening file '{f_name}': {e}")
        print("Data not saved.")
    finally:
        if new_f is not None:
            new_f.close()
        if f is not None:
            f.close()


def read_file(f_name: str) -> None:
    f = None
    try:
        print(f"Accessing file '{f_name}'\n___\n")
        f = open(f_name, "r")
        print(f.read())
    except OSError as e:
        print(f"Error opening file '{f_name}': {e}")
    finally:
        if f is not None:
            f.close()
            print(f"\n___\nFile '{f_name}' closed.")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        read_file(sys.argv[1])
        transform_data(sys.argv[1])


if __name__ == "__main__":
    main()
