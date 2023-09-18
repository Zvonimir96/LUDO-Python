from utilities import button_offset_from_center, display_center, positions_path, buttons_offset, images_size


def create():
    file_object = open(f'{positions_path}/buttons.txt', 'w')

    start1 = display_center[0] - button_offset_from_center - images_size / 2, display_center[1] - images_size / 2
    start2 = display_center[0] - images_size / 2, display_center[1] - button_offset_from_center - images_size / 2
    start3 = display_center[0] + button_offset_from_center - images_size / 2, display_center[1] - images_size / 2
    start4 = display_center[0] - images_size / 2, display_center[1] + button_offset_from_center - images_size / 2

    file_object.write(f'{start1[0]} {start1[1] - buttons_offset} 90\n')
    file_object.write(f'{start1[0]} {start1[1] + buttons_offset} -90\n')
    file_object.write(f'{start1[0]} {start1[1]} -90\n')

    file_object.write(f'{start2[0] + buttons_offset} {start2[1]} 0\n')
    file_object.write(f'{start2[0] - buttons_offset} {start2[1]} 180\n')
    file_object.write(f'{start2[0]} {start2[1]} 180\n')

    file_object.write(f'{start3[0]} {start3[1] - buttons_offset} 90\n')
    file_object.write(f'{start3[0]} {start3[1] + buttons_offset} -90\n')
    file_object.write(f'{start3[0]} {start3[1]} -90\n')

    file_object.write(f'{start4[0] + buttons_offset} {start4[1]} 0\n')
    file_object.write(f'{start4[0] - buttons_offset} {start4[1]} 180\n')
    file_object.write(f'{start4[0]} {start4[1]} 0\n')

    file_object.close()
