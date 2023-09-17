from settings import display_center, path, offset_from_center, offset_fields_x, offset_fields_y

# Houses are moved from center to the top, left, right, and bottom
# House contains four fields witch offset we define
house1_position = (display_center[0] - offset_from_center, display_center[1])
house2_position = (display_center[0], display_center[1] - offset_from_center)
house3_position = (display_center[0] + offset_from_center, display_center[1])
house4_position = (display_center[0], display_center[1] + offset_from_center)

# Save positions to file for each House
file_object = open(f'{path}/house.txt', 'w')

file_object.write(f'{house1_position[0]}, {house1_position[1]}\n')
file_object.write(f'{house1_position[0] - offset_fields_x}, {house1_position[1] - offset_fields_y}\n')
file_object.write(f'{house1_position[0] - offset_fields_x}, {house1_position[1]}\n')
file_object.write(f'{house1_position[0] - offset_fields_x}, {house1_position[1] + offset_fields_y}\n')

file_object.write(f'{house2_position[0]}, {house2_position[1]}\n')
file_object.write(f'{house2_position[0] + offset_fields_x}, {house2_position[1] - offset_fields_y}\n')
file_object.write(f'{house2_position[0]}, {house2_position[1] - offset_fields_y}\n')
file_object.write(f'{house2_position[0] - offset_fields_x}, {house2_position[1] - offset_fields_y}\n')

file_object.write(f'{house3_position[0]}, {house3_position[1]}\n')
file_object.write(f'{house3_position[0] + offset_fields_x}, {house3_position[1] + offset_fields_y}\n')
file_object.write(f'{house3_position[0] + offset_fields_x}, {house3_position[1]}\n')
file_object.write(f'{house3_position[0] + offset_fields_x}, {house3_position[1] - offset_fields_y}\n')

file_object.write(f'{house4_position[0]}, {house4_position[1]}\n')
file_object.write(f'{house4_position[0] - offset_fields_x}, {house4_position[1] + offset_fields_y}\n')
file_object.write(f'{house4_position[0]}, {house4_position[1] + offset_fields_y}\n')
file_object.write(f'{house4_position[0] + offset_fields_x}, {house4_position[1] + offset_fields_y}')

file_object.close()
