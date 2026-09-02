from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Any
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.rank = 0
        self.cache: list[str] = []
        self.stats: list[int] = [0, 0]

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self.cache) < 1:
            return 0, "0"
        self.stats[1] -= 1
        return self.rank, self.cache.pop(0)

    @abstractmethod
    def show_stats(self) -> None:
        pass


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
                    self.stats[0] += 1
                    self.stats[1] += 1
            else:
                self.cache.append(str(data))
                self.stats[0] += 1
                self.stats[1] += 1

    def show_stats(self) -> None:
        print(
            f"Numeric Processor:  total {self.stats[0]} items processed,"
            f" remaining {self.stats[1]} on processor")


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
                    self.stats[0] += 1
                    self.stats[1] += 1
            else:
                self.cache.append(str(data))
                self.stats[0] += 1
                self.stats[1] += 1

    def show_stats(self) -> None:
        print(
            f"Text Processor:  total {self.stats[0]} items processed,"
            f" remaining {self.stats[1]} on processor")


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

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        else:
            if isinstance(data, list):
                for dct in data:
                    self.cache.append(
                        f"{dct['log_level']}: {dct['log_message']}")
                    self.stats[0] += 1
                    self.stats[1] += 1
            else:
                self.cache.append(
                    f"{data['log_level']}: {data['log_message']}")
                self.stats[0] += 1
                self.stats[1] += 1

    def show_stats(self) -> None:
        print(
            f"Log Processor:  total {self.stats[0]} items processed,"
            f" remaining {self.stats[1]} on processor")


class DataStream:

    def __init__(self) -> None:
        self.stream_processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if proc not in self.stream_processors:
            self.stream_processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            for p in self.stream_processors:
                if p.validate(element):
                    p.ingest(element)
                    break
            else:
                print(
                    f"DataStream error - Can't process "
                    f"element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if self.stream_processors:
            for p in self.stream_processors:
                p.show_stats()
        else:
            print("No processor found, no data")


def main() -> None:
    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")

    data = ['Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO',
              'log_message': 'User wil isconnected'}],
            42, ['Hi', 'five']]
    stream = DataStream()
    stream.print_processors_stats()

    num_proc = NumericProcessor()
    print("\nRegistering Numeric Processor")
    stream.register_processor(num_proc)

    print(f"\nSend first batch of data on stream: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    print("Send the same batch again")
    stream.process_stream(data)
    stream.print_processors_stats()

    print("\nConsume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
