from .color import Color

# Path to positions file
positions_path = 'utilities/positions'

# Color
white_color = Color(0, 0, 255)
black_color = Color(0, 0, 0)
red_color = Color(0, 1, 255)

available_colors = [Color(0.1, 1, 255),
                    Color(0.2, 1, 255),
                    Color(0.3, 1, 255),
                    Color(0.4, 1, 255),
                    Color(0.6, 1, 255),
                    Color(0.7, 1, 255),
                    Color(0.8, 1, 255),
                    Color(0.9, 1, 255),
                    Color(1, 1, 255)]

# Images
images_path = './utilities/images/'
images_size = 35

# Layout
path_field_representation = 'large'
house_field_representation = 'large'
safe_house_field_representation = 'large'
dice_field_representation = 'small'

display_width = 800
display_height = 700
display_center = (display_width/2, display_height/2)

path_length = 13
path_line_width = 3

house_exit_index = 2
safe_house_entrance_index = 1

large_circle_size = 16
small_circle_size = 13
circle_line_width = 3

# Dice layout
dice_offset = 25

# Path layout
path_offset_center = 100
path_x = 450
path_y = 200

# Houses layout
house_offset_center = 185
house_offset = 45

# Safe houses layout
safe_house_offset_center = 100
safe_house_offset = 30

# Buttons layout
arrow_image_name = 'arrows/arrow1.png'
submit_name = 'confirm/confirm1.png'
button_offset_from_center = 280
buttons_offset = 50

# Animation
fade_rate = 10
fade_time = 0.05
fade_max_limit = 250
fade_min_limit = 50
fade_alfa = fade_max_limit
fade_direction = False

# Dice roll animation
dice_roll_animation_enabled = False
dice_animation_threshold = 150
dice_animation_increment = 5
dice_animation_counter = 1
dice_animation_change_counter = 0
