def secure_archive(f_name: str, r_or_w: str = "r", content: str = "") -> \
        tuple[bool, str]:
    try:
        if r_or_w == 'r':
            with open(f_name, 'r') as f:
                file_content = f.read()
        elif r_or_w == 'w':
            with open(f_name, 'w') as f:
                f.write(content)
                file_content = content
        else:
            return False, "Error Flag"
    except OSError as e:
        return False, f"{e}"
    return True, file_content


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    t = secure_archive("ancient_fragment1.txt", "r")
    print(t)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    t = secure_archive("ancient_fragment_sec.txt", "r")
    print(t)

    print("\nUsing 'secure_archive' to read from a regular file:")
    t = secure_archive("ancient_fragment.txt", "r")
    print(t)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    t = secure_archive("ancient_fragment.txt", "w",
                       'Content successfully written to file')
    print(t)


if __name__ == "__main__":
    main()
