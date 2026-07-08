# Remember to consider edge cases and check if the input is an integer
# Remove var step

# Calculate max number of moves to solve the challenge
def calculate_steps(number):
    return 2**number-1

def find_cursor(arr: list):
    count = len(arr)
    return count / 2


# Find where the target disk should move
def find_target_rod_pos(current_rod_pos, cursor):
    if current_rod_pos == 0:
        if cursor % 2 == 0:    # cursor=even, goes to the right
            pos = 2

        else:
            pos = 1

    elif current_rod_pos == 1: # cursor=odd, goes to the left
        if cursor % 2 == 0:
            pos = 2

        else:
            pos = 0

    else:
        if cursor % 2 == 0:
            pos = 0

        else:
            pos = 1

    return pos


def is_reverse_sorted(arr, number):
    return len(arr) == number - 1


def rod_pos(number, tower: list[list]):
    pos = 0
    for rod in tower:
        try:
            rod.index(number)
            return pos
        except:
            pos += 1


### MAIN ###
step=1

# Divide and revert sort the array
def reverse_sort(array, tower, position_map, cursor=1):
    cursor += 1

    target_number_rod_pos = position_map.get(array[0])
    target_rod = find_target_rod_pos(target_number_rod_pos, cursor)

    if len(array) == 1:
        #cursor += 1
        print(f'cursor: {cursor}')
        
        disk = array[0]
        print(f"\nFirst target disk: {disk}")

        disk_pos = position_map.get(disk)
        print(f"Disk position in the map before: {disk_pos}")

        current_rod = tower[disk_pos]

        print(f"Target rod: {target_rod}")

        tower[target_rod].append(disk)
        # print(f'Tower after moving the front element: {tower}')

        tower[disk_pos].remove(disk)
        global step
        print(f"# Step {step} - Tower after movement: {tower}")
        step+=1

        position_map[disk] = target_rod  # Records the change in the position map
        print(f"Position map after change: {position_map}")

        return

    target_number = array[0]  # Take the disk to be moved
    rest = array[1:]  # take the rest to be sorted

    #cursor += 1
    print(f'Outside loop cursor:{cursor}')

    # Divide the the array until it is one number and sort
    reverse_sort(                           
        rest, tower, position_map, cursor
    ) 

    print(f'\nArray: {array}')


    # Loop through the array
    for disk in array:
        print(f'\nArray: {array}')
        disk_pos = position_map.get(disk)

        print(f"\nDisk: {disk}")

        print(f"Target rod index: {target_rod}")
        print(f'Inside loop cursor:{cursor}')

        current_rod = tower[disk_pos]
        current_last_disk = min(current_rod)

        # If the disk is not the last item, subdivide again
        if current_last_disk != disk:
            disk_pos_current_rod=current_rod.index(disk)
            rest = current_rod[disk_pos_current_rod+1:]

            print(f'cursor in the loop: {cursor}')

            reverse_sort(
                rest, tower, position_map, cursor
                )  # Subdivide until there is only one disk
            print(f'\nArray: {array}')
        if disk == target_number:
            if disk_pos == target_rod:
                continue

            tower[target_rod].append(disk)
            # print(f'Tower after moving the front element: {tower}')

            print(f"Disk position in the map before: {disk_pos}")

            tower[disk_pos].remove(disk)
            print(f"# Step {step} - Resulting tower: {tower}")
            step+=1

            position_map[disk] = target_rod  # Records the change in the position map
            print(f"Position map after change: {position_map}")

            continue

        # If target rod is empty, transfer the disk to the target
        if not tower[target_rod]:
            tower[target_rod].append(disk)
            # print(f'Tower after moving the front element: {tower}')

            disk_pos = position_map.get(disk)
            print(f"Disk position in the map before: {disk_pos}")

            tower[disk_pos].remove(disk)
            print(f"# Step {step} - Resulting tower: {tower}")
            step+=1

            position_map[disk] = target_rod  # Records the change in the position map
            print(f"Position map after change: {position_map}")

            continue

        target_last_disk = min(tower[target_rod])

        if disk < target_last_disk:
            tower[target_rod].append(disk)
            # print(f'Tower after moving the front element: {tower}')

            disk_pos = position_map.get(disk)
            print(f"Disk position in the map before: {disk_pos}")

            tower[disk_pos].remove(disk)
            print(f"# Step {step} - Resulting tower: {tower}")
            step+=1

            position_map[disk] = target_rod  # Records the change in the position map
            print(f"Position map after change: {position_map}")

    return

    # print(f'{indent}Left side: {left_side}')
    # print(f'{indent}Right side: {right_side}\n')


def hanoi_solver(total_disks):
    first_rod = list(range(total_disks, 0, -1))
    first_rod_pos = 0

    mid_rod = []
    mid_rod_pos = 1

    last_rod = []
    last_rod_pos = 2

    position_map = {}  # Records the initial index of each number in the tower

    for n in first_rod:
        position_map[n] = 0

    hanoi_tower = [first_rod, mid_rod, last_rod]

    indent = "    "

    reverse_sort(first_rod, hanoi_tower, position_map)

    print(position_map)

n=5
hanoi_solver(n)

max_steps=calculate_steps(n)
print(max_steps)