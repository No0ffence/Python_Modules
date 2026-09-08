import importlib.metadata
import importlib
import sys


def close_program(module_name: str) -> None:
    print(f"""
ERROR: Required dependency '{module_name}' is not installed.

Install the dependencies with:
    pip install -r requirements.txt

or with Poetry:
    poetry install
            """)
    sys.exit()


def show_version() -> None:
    print("Packet Name Packet Version")
    for packet in importlib.metadata.distributions():
        print(f"{packet.name} {packet.version}")


def show_info() -> None:
    print("""
=== Package Manager Comparison ===

pip:
  Configuration: requirements.txt
  Install:       pip install -r requirements.txt

Poetry:
  Configuration: pyproject.toml
  Install:       poetry install
    """)


def main() -> None:
    show_info()
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    try:
        pd = importlib.import_module("pandas")
        print(f"[OK] pandas {importlib.metadata.version('pandas')}"
              " - Data manipulation ready")
    except ImportError:
        close_program("pandas")
    try:
        np = importlib.import_module("numpy")
        print(f"[OK] numpy {importlib.metadata.version('numpy')}"
              " - Numerical computation ready")
    except ImportError:
        close_program("numpy")
    try:
        plt = importlib.import_module("matplotlib.pyplot")
        print(f"[OK] matplotlib {importlib.metadata.version('matplotlib')}"
              " -  Visualization ready")
    except ImportError:
        close_program("matplotlib")

    matrix = np.random.randint(1000, size=(10, 10))
    print("Analyzing Matrix data...")
    print(f"Max element: {np.max(matrix)}")
    print(f"Min element: {np.min(matrix)}")
    print(f"AVG element: {np.average(matrix)}")
    print(f"Matrix shape: {matrix.shape}")

    data_frame = pd.DataFrame(matrix)
    print(data_frame)
    print(f"\nPandas info of matrix:\n {data_frame.describe()}")

    print("Generating visualization...")
    plt.imshow(matrix)
    plt.colorbar()
    plt.show()
    print("Analysis complete!")
    show_version()


if __name__ == "__main__":
    main()
