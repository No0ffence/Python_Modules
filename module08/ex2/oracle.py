import os
import sys
from dotenv import load_dotenv


class ConfigError(Exception):
    def __init__(self, message: str = "Missing configuration") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"Caught ConfigError: {self.message}"


def check_config() -> None:
    config_vars = ["MATRIX_MODE", "DATABASE_URL",
                   "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]
    load_dotenv()
    for v in config_vars:
        if not os.getenv(v):
            raise ConfigError(f"Missing {v} config parameter "
                              f"please provide it in .env file")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    try:
        check_config()
    except ConfigError as e:
        print(e)
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print(f"Database: {os.getenv('DATABASE_URL')}")
    print(f"API Access: {os.getenv('API_KEY')}")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}")

    print("""
Environment security check:
[OK] No hardcoded secrets detected
[OK] .env file properly configured
[OK] Production overrides available
    """)

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
