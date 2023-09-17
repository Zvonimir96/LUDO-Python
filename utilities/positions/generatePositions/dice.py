from settings import display_center, path, dice_offset

file_object = open(f'{path}/dice.txt', 'w')

file_object.write(f'{display_center[0] - dice_offset}, {display_center[1] - dice_offset}\n')
file_object.write(f'{display_center[0]}, {display_center[1] - dice_offset}\n')
file_object.write(f'{display_center[0] + dice_offset}, {display_center[1] - dice_offset}\n')

file_object.write(f'{display_center[0] + dice_offset}, {display_center[1]}\n')
file_object.write(f'{display_center[0] + dice_offset}, {display_center[1] + dice_offset}\n')

file_object.write(f'{display_center[0]}, {display_center[1] + dice_offset}\n')
file_object.write(f'{display_center[0] - dice_offset}, {display_center[1] + dice_offset}\n')

file_object.write(f'{display_center[0] - dice_offset}, {display_center[1]}\n')

file_object.write(f'{display_center[0]}, {display_center[1]}\n')

file_object.close()