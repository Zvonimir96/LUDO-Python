import pygame
import numpy

filename = '../resources/confirmSet.png'

image = pygame.image.load(filename)
image = pygame.transform.rotate(image, 50)
image = pygame.transform.scale(image, (200, 200))
arr = pygame.surfarray.pixels3d(image)

test = numpy.empty((0, 3), int)
test = numpy.append(test, [arr[0, 0]], axis=0)

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        arrayExist = False

        for k in range(test.shape[0]):
            if numpy.array_equal(numpy.array(arr[i, j]), test[k]):
                arrayExist = True
                break

        if not arrayExist:
            test = numpy.append(test, [arr[i, j]], axis=0)

print(test)
