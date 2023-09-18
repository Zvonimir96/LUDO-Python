from utilities import positions_path, display_center, dice_offset


def create():
    file_object = open(f'{positions_path}/dice.txt', 'w')

    file_object.write(f'{display_center[0] - dice_offset} {display_center[1] - dice_offset}\n')
    file_object.write(f'{display_center[0]} {display_center[1] - dice_offset}\n')
    file_object.write(f'{display_center[0] + dice_offset} {display_center[1] - dice_offset}\n')

    file_object.write(f'{display_center[0] + dice_offset} {display_center[1]}\n')
    file_object.write(f'{display_center[0] + dice_offset} {display_center[1] + dice_offset}\n')

    file_object.write(f'{display_center[0]} {display_center[1] + dice_offset}\n')
    file_object.write(f'{display_center[0] - dice_offset} {display_center[1] + dice_offset}\n')

    file_object.write(f'{display_center[0] - dice_offset} {display_center[1]}\n')

    file_object.write(f'{display_center[0]} {display_center[1]}\n')

    file_object.close()
