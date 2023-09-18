from utilities import display_center, positions_path, safe_house_offset_center, safe_house_offset


def create():
    house1_position = (display_center[0] - safe_house_offset_center, display_center[1] - safe_house_offset_center)
    house2_position = (display_center[0] + safe_house_offset_center, display_center[1] - safe_house_offset_center)
    house3_position = (display_center[0] + safe_house_offset_center, display_center[1] + safe_house_offset_center)
    house4_position = (display_center[0] - safe_house_offset_center, display_center[1] + safe_house_offset_center)

    file_object = open(f'{positions_path}/safeHouse.txt', 'w')

    for i in range(4):
        file_object.write(f'{house1_position[0] - safe_house_offset * i} {house1_position[1] - safe_house_offset * i}\n')

    for i in range(4):
        file_object.write(f'{house2_position[0] + safe_house_offset * i} {house2_position[1] - safe_house_offset * i}\n')

    for i in range(4):
        file_object.write(f'{house3_position[0] + safe_house_offset * i} {house3_position[1] + safe_house_offset * i}\n')

    for i in range(4):
        file_object.write(f'{house4_position[0] - safe_house_offset * i} {house4_position[1] + safe_house_offset * i}\n')

    file_object.close()