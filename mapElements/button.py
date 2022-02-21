import pygame

from settings import numberOfArrowImages, arrowImageName, blackColor
from settings import numberOfConfirmImages, confirmImageName
from settings import imageScale


class Button:
    buttons = []
    buttonNumber = 0

    def __init__(self, position, angle, imageType, enabled=True):
        Button.buttons.append(self)

        self.buttonNumber = Button.buttonNumber
        Button.buttonNumber = Button.buttonNumber + 1

        self.width = None
        self.height = None
        self.image = None
        self.angle = angle
        self.position = position
        self.imageNumber = 0
        self.imageType = imageType
        self.enabled = enabled

        self.changeImage()

    def changeImage(self):
        self.imageNumber = self.imageNumber + 1

        if self.imageType == 0:
            maxImageNumber = numberOfArrowImages
        else:
            maxImageNumber = numberOfConfirmImages

        if self.imageNumber >= maxImageNumber:
            self.imageNumber = 1

        if self.imageType == 0:
            self.image = pygame.image.load(arrowImageName.replace('%', str(self.imageNumber)))
        else:
            self.image = pygame.image.load(confirmImageName.replace('%', str(self.imageNumber)))

        self.image = pygame.transform.rotate(self.image, self.angle)
        self.height = self.image.get_height() / imageScale
        self.width = self.image.get_width() / imageScale
        self.image = pygame.transform.scale(self.image, (self.height, self.width))

    def draw(self, screen):
        if self.enabled:
            screen.blit(self.image, (self.position[0] - self.width / 2, self.position[1] - self.height / 2))

    def changeColor(self, color):
        imageArray = pygame.surfarray.pixels3d(self.image)

        for i in range(imageArray.shape[0]):
            for j in range(imageArray.shape[1]):
                if imageArray[i, j, 0] > 150 or imageArray[i, j, 1] > 150 or imageArray[i, j, 2] > 150:
                    imageArray[i, j] = color
                else:
                    imageArray[i, j] = (0, 0, 0)

    def isButtonClicked(self, mousePosition):
        if (self.position[0] - self.width / 2) < mousePosition[0] < (self.position[0] + self.width / 2) and \
                (self.position[1] - self.height / 2) < mousePosition[1] < (self.position[1] + self.height / 2) and \
                self.enabled == True:
            return self.buttonNumber
        return -1

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    @staticmethod
    def isAnyButtonClicked(mousePosition):
        for button in Button.buttons:
            buttonNumber = button.isButtonClicked(mousePosition)
            if buttonNumber != -1:
                return buttonNumber

    @staticmethod
    def changeImages():
        for button in Button.buttons:
            button.changeImage()

    @staticmethod
    def drawAll(screen):
        for button in Button.buttons:
            button.draw(screen)

    @staticmethod
    def create():
        Button((300, 200), 45, 0)
        Button((200, 300), 225, 0)
        Button((250, 250), 0, 1)

        Button((700, 200), 135, 0)
        Button((800, 300), 315, 0)
        Button((750, 250), 0, 1)

        Button((700, 800), 225, 0)
        Button((800, 700), 45, 0)
        Button((750, 750), 0, 1)

        Button((300, 800), 315, 0)
        Button((200, 700), 135, 0)
        Button((250, 750), 0, 1)
