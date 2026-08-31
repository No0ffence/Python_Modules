import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["BOB", "Alice", "charlie", "vecha"]
    actions = ["eat", "sleep", "swim", "fly"]
    while True:
        yield random.choice(players), random.choice(actions)


def consume_event(lst: list[tuple[str, str]]) \
        -> typing.Generator[tuple[str, str], None, None]:
    while lst:
        element = random.choice(lst)
        lst.remove(element)
        yield element


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generator = gen_event()
    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list = []
    for i in range(10):
        event = next(generator)
        event_list.append(event)

    print(f"Built list of {len(event_list)} events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
