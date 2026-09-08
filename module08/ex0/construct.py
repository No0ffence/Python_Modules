import sys
import site


def in_venv() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}\n"
          f"Virtual Environment: {sys.prefix.split('/')[-1]}")

    print("""
SUCCESS: You're in an isolated environment!
Safe to install packages without affecting
the global system.
    """)

    print("Package installation path: \n"
          f"{site.getsitepackages()[0]}")


def out_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}\n"
          "Virtual Environment: None detected")

    print("""
WARNING: You're in the global environment!
The machines can see everything you install.
To enter the construct, run:
python -m venv matrix_env
source matrix_env/bin/activate # On Unix
matrix_env\\Scripts\\activate # On Windows
Then run this program again.
    """)


def main() -> None:
    if sys.prefix != sys.base_prefix:
        in_venv()
    else:
        out_venv()


if __name__ == "__main__":
    main()
