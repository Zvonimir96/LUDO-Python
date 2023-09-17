import math

from settings import display_center, path_length, offset_from_center, offset_x, offset_y, path

# Class that helps calculate bezier curve with four control points
# Bezier curve is used to create path for figures
class Bezier:
    def __init__(self, P0, P1, P2, P3):
        self.P0 = P0
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3

    # Path contains dots that are drawn on some curvature
    # By applying this mathematical function, we can generate positions on curvature by applying t in range 0 to 1
    def calc(self, t):
        return ((1 - t) ** 3 * self.P0[0] + 3 * t * (1 - t) ** 2 * self.P1[0] + 3 * t ** 2 * (1 - t) * self.P2[
            0] + t ** 3 * self.P3[0],
                (1 - t) ** 3 * self.P0[1] + 3 * t * (1 - t) ** 2 * self.P1[1] + 3 * t ** 2 * (1 - t) * self.P2[
                    1] + t ** 3 * self.P3[1])


# Set bezier control points
bezUp = Bezier((display_center[0] - offset_from_center, display_center[1]),
               (display_center[0] - offset_x, display_center[1] - offset_y),
               (display_center[0] - offset_y, display_center[1] - offset_x),
               (display_center[0], display_center[1] - offset_from_center))
bezLeft = Bezier((display_center[0], display_center[1] - offset_from_center),
                 (display_center[0] + offset_y, display_center[1] - offset_x),
                 (display_center[0] + offset_x, display_center[1] - offset_y),
                 (display_center[0] + offset_from_center, display_center[1]))
bezDown = Bezier((display_center[0] + offset_from_center, display_center[1]),
                 (display_center[0] + offset_x, display_center[1] + offset_y),
                 (display_center[0] + offset_y, display_center[1] + offset_x),
                 (display_center[0], display_center[1] + offset_from_center))
bezRight = Bezier((display_center[0], display_center[1] + offset_from_center),
                  (display_center[0] - offset_y, display_center[1] + offset_x),
                  (display_center[0] - offset_x, display_center[1] + offset_y),
                  (display_center[0] - offset_from_center, display_center[1]))

# Function that generates positions on curvature gives nonlinear distance between positions
# We need to perform mathematical equation on t so that function can produce points with same distance between each other
x1 = 1
x2 = int(math.ceil(path_length / 2))
y1 = 0.5
y2 = 1.418
t = [0] * 1

for i in range(path_length):
    if i < path_length / 2:
        x = i + 1
    else:
        x = path_length - i

    scale = (y2 - y1) / (x2 - x1) * (x - x1) + y1
    step = 1 / (path_length - 1) * scale
    t.append(t[i] + step)

# Save positions to file for each curve
file_object = open(f'{path}/path.txt', 'w')

for i in range(path_length):
    position = bezUp.calc(t[i])
    file_object.write(f'{position[0]}, {position[1]}\n')

for i in range(path_length):
    position = bezLeft.calc(t[i])
    file_object.write(f'{position[0]}, {position[1]}\n')

for i in range(path_length):
    position = bezDown.calc(t[i])
    file_object.write(f'{position[0]}, {position[1]}\n')

for i in range(path_length):
    position = bezRight.calc(t[i])
    file_object.write(f'{position[0]}, {position[1]}\n')

file_object.close()