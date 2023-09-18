from utilities import display_center, positions_path, house_offset_center, house_offset


def create():
    # House contains four fields
    house1_position = (display_center[0] - house_offset_center, display_center[1])
    house2_position = (display_center[0], display_center[1] - house_offset_center)
    house3_position = (display_center[0] + house_offset_center, display_center[1])
    house4_position = (display_center[0], display_center[1] + house_offset_center)

    # Save positions to file for each House
    file_object = open(f'{positions_path}/house.txt', 'w')

    file_object.write(f'{house1_position[0]} {house1_position[1]}\n')
    file_object.write(f'{house1_position[0] - house_offset} {house1_position[1] - house_offset}\n')
    file_object.write(f'{house1_position[0] - house_offset} {house1_position[1]}\n')
    file_object.write(f'{house1_position[0] - house_offset} {house1_position[1] + house_offset}\n')

    file_object.write(f'{house2_position[0]} {house2_position[1]}\n')
    file_object.write(f'{house2_position[0] + house_offset} {house2_position[1] - house_offset}\n')
    file_object.write(f'{house2_position[0]} {house2_position[1] - house_offset}\n')
    file_object.write(f'{house2_position[0] - house_offset} {house2_position[1] - house_offset}\n')

    file_object.write(f'{house3_position[0]} {house3_position[1]}\n')
    file_object.write(f'{house3_position[0] + house_offset} {house3_position[1] + house_offset}\n')
    file_object.write(f'{house3_position[0] + house_offset} {house3_position[1]}\n')
    file_object.write(f'{house3_position[0] + house_offset} {house3_position[1] - house_offset}\n')

    file_object.write(f'{house4_position[0]} {house4_position[1]}\n')
    file_object.write(f'{house4_position[0] - house_offset} {house4_position[1] + house_offset}\n')
    file_object.write(f'{house4_position[0]} {house4_position[1] + house_offset}\n')
    file_object.write(f'{house4_position[0] + house_offset} {house4_position[1] + house_offset}')

    file_object.close()
