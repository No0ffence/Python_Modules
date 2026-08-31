import math


def check_input(arr: list[str]) -> bool:
    if len(arr) != 3:
        print("Invalid syntax")
        return False
    for i in arr:
        try:
            float(i)
        except ValueError as e:
            print(f"Error on parameter '{i}': {e}")
            return False
    return True


def get_player_pos() -> tuple[float, float, float]:
    while True:
        inp = input("Enter new coordinates as "
                    "floats in format 'x,y,z': ").replace(",", " ").split()

        if check_input(inp):
            arr = (float(inp[0]), float(inp[1]), float(inp[2]))
            break
    return arr


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    cords1 = get_player_pos()
    print(f"Got a first tuple: {cords1}")
    print(f"It includes: X={cords1[0]}, Y={cords1[1]}, Z={cords1[2]}")
    dst_to_center = math.sqrt((0 - cords1[0]) ** 2 + (0 - cords1[1]) ** 2 +
                              (0 - cords1[2]) ** 2)
    print(f"Distance to center: {round(dst_to_center, 4)}")

    print("\nGet a second set of coordinates")
    cords2 = get_player_pos()
    print(f"Got a second tuple: {cords2}")
    print(f"It includes: X={cords2[0]}, Y={cords2[1]}, Z={cords2[2]}")
    dst_to_second = math.sqrt(
        (cords2[0] - cords1[0]) ** 2 + (cords2[1] - cords1[1]) ** 2 + (
                cords2[2] - cords1[2]) ** 2)
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(dst_to_second, 4)}")


if __name__ == "__main__":
    main()
