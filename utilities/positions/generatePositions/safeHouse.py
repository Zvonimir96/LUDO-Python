from settings import display_center, path, offset_from_center, offset_fields_x, offset_fields_y

offset = 30
offsetFromCenter = 100

house1_position = (display_center[0] - offsetFromCenter, display_center[1] - offsetFromCenter)
house2_position = (display_center[0] + offsetFromCenter, display_center[1] - offsetFromCenter)
house3_position = (display_center[0] + offsetFromCenter, display_center[1] + offsetFromCenter)
house4_position = (display_center[0] - offsetFromCenter, display_center[1] + offsetFromCenter)

file_object = open(f'{path}/safeHouse.txt', 'w')

for i in range(4):
    file_object.write(f'{house1_position[0] - offset * i}, {house1_position[1] - offset * i}\n')

for i in range(4):
    file_object.write(f'{house2_position[0] + offset * i}, {house2_position[1] - offset * i}\n')

for i in range(4):
    file_object.write(f'{house3_position[0] + offset * i}, {house3_position[1] + offset * i}\n')

for i in range(4):
    file_object.write(f'{house4_position[0] - offset * i}, {house4_position[1] + offset * i}\n')

file_object.close()