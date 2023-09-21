import pygame
from utilities import images_size, fade_rate, fade_max_limit, fade_min_limit, images_path


class Button:
    def __init__(self, draw_position, rotation, image_name):
        # Screen x and y positions
        self.draw_position = draw_position

        # Button can be disabled
        self.enabled = True

        # Set button image
        self.image = pygame.image.load(images_path + image_name)
        self.image = pygame.transform.rotate(self.image, rotation)
        self.image = pygame.transform.scale(self.image, (images_size, images_size))

    def draw(self, screen):
        screen.blit(self.image, (self.draw_position[0], self.draw_position[1]))

    def change_color(self, color):
        imageArray = pygame.surfarray.pixels3d(self.image)

        # Change color of each pixel
        for i in range(imageArray.shape[0]):
            for j in range(imageArray.shape[1]):
                if imageArray[i, j, 0] > 50 or imageArray[i, j, 1] > 50 or imageArray[i, j, 2] > 50:
                    imageArray[i, j] = color.to_rgb()
                else:
                    imageArray[i, j] = (0, 0, 0)
