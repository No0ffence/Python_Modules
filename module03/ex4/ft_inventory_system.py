import sys


def check_argument(arg: str) -> int:
    two_elements_arr = arg.split(":")
    if len(two_elements_arr) != 2:
        print(f"Error - invalid parameter {two_elements_arr}")
        return 0
    try:
        int(two_elements_arr[1])
    except ValueError as e:
        print(
            f"Quantity error for '{two_elements_arr[0]}': {e}")
        return 0
    return 1


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}
    for arg in sys.argv[1:]:
        if check_argument(arg) == 1:
            inventory.update({arg.split(":")[0]: int(arg.split(":")[1])})

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(
        f"Total quantity of the "
        f"{len(inventory)} items: {sum(inventory.values())}")

    for key in inventory.keys():
        print(
            f"Item {key} represents "
            f"{round(inventory[key] / sum(inventory.values()) * 100, 1)}%"
        )

    if inventory:
        max_key = list(inventory.keys())[0]
        max_value = inventory[max_key]
        min_key = list(inventory.keys())[0]
        min_value = inventory[min_key]
        for key in inventory.keys():
            if max_value < inventory[key]:
                max_value = inventory[key]
                max_key = key
            if min_value > inventory[key]:
                min_value = inventory[key]
                min_key = key
        print(f"Item most abundant: {max_key} with quantity {max_value}")
        print(f"Item least abundant: {min_key} with quantity {min_value}")
    else:
        print("inventory empty")

    item = {"magic_item": 1}
    inventory.update(item)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
