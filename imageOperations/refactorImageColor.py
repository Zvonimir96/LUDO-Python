import pygame

filename = '../resources/confirmSet.png'

image = pygame.image.load(filename)
imageArray = pygame.surfarray.pixels3d(image)

for i in range(imageArray.shape[0]):
    for j in range(imageArray.shape[1]):
        if imageArray[i, j, 0] > 125 and imageArray[i, j, 1] > 125 and imageArray[i, j, 2] > 125:
            imageArray[i, j] = [0, 0, 0]
        else:
            imageArray[i, j] = [255, 255, 255]

image = pygame.surfarray.make_surface(imageArray)

pygame.image.save(image, '../resources/confirmSet2.png')
