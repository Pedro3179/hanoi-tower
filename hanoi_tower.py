'''
Solve the mathematical puzzle known as the Tower of Hanoi. The puzzle consists of three rods
and a number of disks of different diameters.

The puzzle starts with the disks piled up on the first rod, in decreasing size,
with the smallest disk on top and the largest disk on the bottom.

The goal of the Tower of Hanoi puzzle is moving all the disks to the last rod. To do that,
you must follow three simple rules:

1. You can move only top-most disks.
2. You can move only one disk at a time.
3. You cannot place larger disks on top of smaller ones.
'''


# Calculate the maximum number of moves
def calculate_steps(number):
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    return 2**number - 1


# Check whether an array is reverse-sorted:
def is_reverse_sorted(arr):
    if not arr:
        return True

    if len(arr) == 1:
        return True

    return arr == sorted(arr, reverse=True)


### MAIN ###


def hanoi_solver(total_disks):
    # Check if the input is an integer
    if not isinstance(total_disks, int):
        raise TypeError("Input must be an integer.")

    # Find where the selected disk should move
    def find_target_rod_pos(current_rod_pos, previous_target):
        positions = (0, 1, 2)

        for pos in positions:
            if pos == current_rod_pos or pos == previous_target:
                continue

            return pos

    # Generate the list of numbers in the first rod
    first_rod = list(range(total_disks, 0, -1))

    position_map = {}  # Stores the rod position of each disk

    for n in first_rod:
        position_map[n] = 0

    hanoi_tower = [
        list(first_rod),
        [],
        [],
    ]  # Tower state that will be modified while solving the puzzle

    output_string = f"{hanoi_tower[0]} {hanoi_tower[1]} {hanoi_tower[2]}"  # Output produced by hanoi_solver()

    # Recursively reverse-sort the tower of hanoi
    def reverse_sort(array, tower, position_map, output_string, previous_target=1):
        target_number_rod_pos = position_map.get(array[0])
        target_rod = find_target_rod_pos(target_number_rod_pos, previous_target)
        previous_target = target_rod

        if len(array) == 1:

            disk = array[0]

            disk_pos = position_map.get(disk)

            current_rod = tower[disk_pos]

            tower[target_rod].append(disk)

            tower[disk_pos].remove(disk)

            output_string += f"\n{tower[0]} {tower[1]} {tower[2]}"

            position_map[disk] = target_rod  # Records the change in the position map
            # print(f"Position map after change: {position_map}")

            return output_string

        target_number = array[0]  # Select the disk to move
        rest = array[1:]  # Remaining disks to process

        # Recursively split the array until it is only one disk and sort it
        output_string = reverse_sort(
            rest, tower, position_map, output_string, previous_target
        )

        # Move each disk to the target rod
        for disk in array:
            disk_pos = position_map.get(disk)

            current_rod = tower[disk_pos]
            current_last_disk = min(current_rod)

            # If the disk is not the last item, recursively split again
            if current_last_disk != disk:
                disk_pos_current_rod = current_rod.index(disk)
                rest = current_rod[disk_pos_current_rod + 1 :]

                output_string = reverse_sort(
                    rest, tower, position_map, output_string, previous_target
                )

            if disk == target_number:
                if disk_pos == target_rod:
                    continue

                tower[target_rod].append(disk)

                tower[disk_pos].remove(disk)

                output_string += f"\n{tower[0]} {tower[1]} {tower[2]}"

                position_map[disk] = (
                    target_rod  # Records the change in the position map
                )

                continue

            target_last_disk = min(tower[target_rod])

            if disk < target_last_disk:
                tower[target_rod].append(disk)

                disk_pos = position_map.get(disk)

                tower[disk_pos].remove(disk)

                output_string += f"\n{tower[0]} {tower[1]} {tower[2]}"

                position_map[disk] = (
                    target_rod  # Records the change in the position map
                )

        return output_string

    # print(f"Last rod is reverse-sorted: {is_reverse_sorted(hanoi_tower[2])}")

    return reverse_sort(first_rod, hanoi_tower, position_map, output_string)


n = 5

ht = hanoi_solver(n)

print(ht)

max_steps = calculate_steps(n)
# print(f"Max number of steps: {max_steps}")
