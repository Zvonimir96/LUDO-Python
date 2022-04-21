import pygame

from mapElements.neopixel import Neopixel
from settings import imageScale, fadeRate, fadeMaxLimit, fadeMinLimit


class Button(Neopixel):
    buttonNumber = 0
    buttons = []

    def __init__(self, position, angle, maxImageNumber, imageName):
        super().__init__(position)
        Button.buttons.append(self)

        self.angle = angle
        self.maxImageNumber = maxImageNumber
        self.imageName = imageName
        self.alfa = 255

        self.fading = False
        self.fadeUp = False

        self.buttonNumber = Button.buttonNumber
        Button.buttonNumber = Button.buttonNumber + 1

        self.width = None
        self.height = None
        self.image = None

        self.imageNumber = 1
        self.enabled = False

        self.changeImage()

    def setFade(self):
        self.fading = True

    def disableFade(self):
        self.fading = False

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def setColor(self, color):
        super().setColor(color)
        self.changeColor()

    def draw(self, screen):
        if self.enabled:
            screen.blit(self.image, (self.position[0] - self.width / 2, self.position[1] - self.height / 2))

    def changeImage(self):
        self.imageNumber = self.imageNumber + 1

        if self.imageNumber >= self.maxImageNumber:
            self.imageNumber = 1

        self.image = pygame.image.load(self.imageName.replace('%', str(self.imageNumber)))

        self.image = pygame.transform.rotate(self.image, self.angle)
        self.height = self.image.get_height() / imageScale
        self.width = self.image.get_width() / imageScale
        self.image = pygame.transform.scale(self.image, (self.height, self.width))

    def changeColor(self):
        imageArray = pygame.surfarray.pixels3d(self.image)

        for i in range(imageArray.shape[0]):
            for j in range(imageArray.shape[1]):
                if imageArray[i, j, 0] > 50 or imageArray[i, j, 1] > 50 or imageArray[i, j, 2] > 50:
                    imageArray[i, j] = self.color.get()
                else:
                    imageArray[i, j] = (0, 0, 0)

    def isButtonClicked(self, mousePosition):
        if (self.position[0] - self.width / 2) < mousePosition[0] < (self.position[0] + self.width / 2) and \
                (self.position[1] - self.height / 2) < mousePosition[1] < (self.position[1] + self.height / 2) and \
                self.enabled:
            return self.buttonNumber
        return -1

    def fade(self):
        if self.fadeUp:
            self.alfa += fadeRate
        else:
            self.alfa -= fadeRate

        if self.alfa >= fadeMaxLimit:
            self.alfa = fadeMaxLimit
            self.fadeUp = False
        elif self.alfa <= fadeMinLimit:
            self.alfa = fadeMinLimit
            self.fadeUp = True

        self.image.set_alpha(self.alfa)

    @staticmethod
    def fadeAll():
        for button in Button.buttons:
            if button.fading:
                button.fade()

    @staticmethod
    def isAnyButtonClicked(mousePosition):
        for button in Button.buttons:
            buttonNumber = button.isButtonClicked(mousePosition)
            if buttonNumber != -1:
                return buttonNumber

        return -1

    @staticmethod
    def drawAll(screen):
        for button in Button.buttons:
            button.draw(screen)
