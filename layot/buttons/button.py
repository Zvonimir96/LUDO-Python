import pygame

from utilities import images_size, images_path


class Button:
    def __init__(self, draw_position, rotation, image_name):
        """
        Handle and display button image. This class does not support button click.

        :param draw_position: position on screen where field will be drawn.
        :param rotation: image rotation.
        :param image_name: image name to be drawn.
        """

        self.draw_position = draw_position

        # Button can be disabled
        self.enabled = True

        # Set button image, rotation and scale
        self.image = pygame.image.load(images_path + image_name)
        self.image = pygame.transform.rotate(self.image, rotation)
        self.image = pygame.transform.scale(self.image, (images_size, images_size))

    def draw(self, screen):
        screen.blit(self.image, (self.draw_position[0], self.draw_position[1]))

    def set_color(self, color):
        imageArray = pygame.surfarray.pixels3d(self.image)

        # Change color of each pixel
        for i in range(imageArray.shape[0]):
            for j in range(imageArray.shape[1]):
                if imageArray[i, j, 0] > 50 or imageArray[i, j, 1] > 50 or imageArray[i, j, 2] > 50:
                    imageArray[i, j] = color.to_rgb()
                else:
                    imageArray[i, j] = (0, 0, 0)
