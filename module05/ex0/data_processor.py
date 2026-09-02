from abc import ABC, abstractmethod
from typing import Any
from collections.abc import Sequence


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.rank = 0
        self.cache: list[str] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self.cache) < 1:
            return 0, "0"
        return self.rank, self.cache.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.rank = 1

    def validate(self, data: Any) -> bool:
        return (isinstance(data, (int, float))
                or isinstance(data, list) and
                all(isinstance(x, (int, float)) for x in data))

    def ingest(self, data: int | float | Sequence[int | float]) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        else:
            if isinstance(data, list):
                for i in data:
                    self.cache.append(str(i))
            else:
                self.cache.append(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.rank = 2

    def validate(self, data: Any) -> bool:
        return (isinstance(data, str)
                or isinstance(data, list) and
                all(isinstance(x, str) for x in data))

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        else:
            if isinstance(data, list):
                for i in data:
                    self.cache.append(str(i))
            else:
                self.cache.append(str(data))


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.rank = 3

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                    all(isinstance(k, str) and isinstance(v, str)
                        for k, v in data.items())
                    and "log_level" in data
                    and "log_message" in data
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(isinstance(k, str) for k in item.keys())
                and all(isinstance(v, str) for v in item.values())
                and "log_level" in item
                and "log_message" in item
                for item in data
            )

        return False

        # return (isinstance(data, list) and all(
        #     isinstance(x, dict) and all(
        #         isinstance(k, str) for k in x.keys()) and all(
        #         isinstance(v, str) for v in x.values()) for x in data)
        #         or isinstance(data, dict) and
        #         all(isinstance(k, str) for k in data.keys()) and all(
        #             isinstance(v, str) for v in data.values()))

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        else:
            if isinstance(data, list):
                for dct in data:
                    self.cache.append(
                        f"{dct['log_level']}: {dct['log_message']}")
            else:
                self.cache.append(
                    f"{data['log_level']}: {data['log_message']}")


def check_num() -> None:
    print("\nTesting Numeric Processor...")
    num = NumericProcessor()

    for i in [42, "hello"]:
        print(f"Trying to validate input '{i}: {num.validate(i)}")

    err_inp = "foo"
    print(
        f"Test invalid ingestion of string "
        f"'{err_inp}' without prior validation:")
    try:
        num.ingest(err_inp)
    except TypeError as e:
        print(f"Got exception: {e}")
    try:
        num_lst = [1, 2, 3, 4, 5]
        print(f"Processing data: {num_lst}")
        num.ingest(num_lst)
        print(f"Extracting {len(num.cache)} values...")
        for i in range(0, len(num.cache)):
            print(f"Numeric value {i}: {num.output()[1]}")
    except TypeError as e:
        print(f"Got exception: {e}")


def check_text() -> None:
    print("\nTesting Text Processor...")
    text = TextProcessor()
    for i in [42, "hello", "67", "52"]:
        print(f"Trying to validate input '{i}': {text.validate(i)}")

    txt_data = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {txt_data}")
    try:
        text.ingest(txt_data)
        print(f"Extracting {len(text.cache)} values...")
        for i in range(0, len(text.cache)):
            print(f"Text value {i}: {text.output()[1]}")
    except TypeError as e:
        print(f"Got exception: {e}")


def check_log() -> None:
    print("\nTesting Log Processor...")
    log = LogProcessor()
    print(f"Trying to validate input 'Hello: {log.validate('Hello')}")
    dct = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
           {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    print(f"Trying to validate input '{dct}: {log.validate(dct)}")
    try:
        print(f"Prcessing data: {dct}")
        log.ingest(dct)
        print(f"Extracting {len(log.cache)} values...")
        for i in range(0, len(log.cache)):
            print(f"Log entry {i}: {log.output()[1]}")
    except TypeError as e:
        print(f"Got exception: {e}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    check_num()
    check_text()
    check_log()


if __name__ == "__main__":
    main()
