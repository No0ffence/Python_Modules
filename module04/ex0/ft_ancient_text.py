import sys


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
        print("=== Cyber Archives Recovery ===")
        read_file(sys.argv[1])


if __name__ == "__main__":
    main()
