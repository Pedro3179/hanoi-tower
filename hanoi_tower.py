# Remember to consider edge cases and check if the input is an integer
# Remove var step


# Calculate max number of moves to solve the challenge
def calculate_steps(number):
    if not isinstance(number, int):
        raise TypeError('Input must be an integer.')

    return 2**number - 1


# Check whether an array is reverse sorted:
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
        raise TypeError('Input must be an integer.')

    # Find where the target disk should move
    def find_target_rod_pos(current_rod_pos, previous_target):
        positions = (0, 1, 2)

        for pos in positions:
            if pos == current_rod_pos or pos == previous_target:
                continue

            return pos
        
    # Generate the list of numbers in the first rod
    first_rod = list(
        range(total_disks, 0, -1)
    ) 

    position_map = {}  # Records the initial index of each number in the tower

    for n in first_rod:
        position_map[n] = 0

    hanoi_tower = [list(first_rod), [], []]

    output_string=f'{hanoi_tower[0]} {hanoi_tower[1]} {hanoi_tower[2]}'

    # Divide and revert sort the tower of hanoi
    def reverse_sort(
            array, tower, position_map, output_string, previous_target=1
            ):
        target_number_rod_pos = position_map.get(array[0])
        target_rod = find_target_rod_pos(target_number_rod_pos, previous_target)
        previous_target = target_rod

        if len(array) == 1:

            disk = array[0]

            disk_pos = position_map.get(disk)

            current_rod = tower[disk_pos]

            tower[target_rod].append(disk)

            tower[disk_pos].remove(disk)

            output_string+=f'\n{tower[0]} {tower[1]} {tower[2]}'

            position_map[disk] = target_rod  # Records the change in the position map
            # print(f"Position map after change: {position_map}")

            return output_string

        target_number = array[0]  # Take the disk to be moved
        rest = array[1:]  # take the rest to be sorted

        # Divide the the array until it is one number and sort
        output_string=reverse_sort(rest, tower, position_map, output_string, previous_target)


        # Loop through the array
        for disk in array:
            disk_pos = position_map.get(disk)

            current_rod = tower[disk_pos]
            current_last_disk = min(current_rod)

            # If the disk is not the last item, subdivide again
            if current_last_disk != disk:
                disk_pos_current_rod = current_rod.index(disk)
                rest = current_rod[disk_pos_current_rod + 1 :]
                # print(f'Rest: {rest}')

                # print(f'Previous target in the loop: {previous_target}')

                output_string=reverse_sort(
                    rest,
                    tower, 
                    position_map,
                    output_string,
                    previous_target
                )

            if disk == target_number:
                if disk_pos == target_rod:
                    continue

                tower[target_rod].append(disk)

                tower[disk_pos].remove(disk)

                output_string+=f'\n{tower[0]} {tower[1]} {tower[2]}'

                position_map[disk] = (
                    target_rod  # Records the change in the position map
                )

                continue

            target_last_disk = min(tower[target_rod])

            if disk < target_last_disk:
                tower[target_rod].append(disk)

                disk_pos = position_map.get(disk)

                tower[disk_pos].remove(disk)
                
                output_string+=f'\n{tower[0]} {tower[1]} {tower[2]}'

                position_map[disk] = (
                    target_rod  # Records the change in the position map
                )

        return output_string

    #print(f"Last Array is reverse sorted: {is_reverse_sorted(hanoi_tower[2])}")

    return reverse_sort(first_rod, hanoi_tower, position_map, output_string)

n = 5

ht=hanoi_solver(n)

print(ht)

max_steps = calculate_steps(n)
#print(f"Max number of steps: {max_steps}")

