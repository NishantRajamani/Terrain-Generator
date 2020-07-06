import noise
import numpy as np
import cv2

shape = (1024, 1024)
scale = 1 #number that determines at what distance to view the noisemap
octaves = 1 #the number of levels of detail you want you perlin noise to have
persistence = 1.0 # number that determines how much detail is added or removed at each octave (adjusts frequency)
lacunarity = 0 #number that determines how much each octave contributes to the overall shape (adjusts amplitude)

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=0)
# print(world.min(), world.max())
# world += 1
# print(world.min(), world.max())
# world *= 255
# print(world.min(), world.max())
# world /= 2
# print(world.min(), world.max())
# cv2.imwrite(r"world1.png", world)
# world += 1
# world /= 2
cv2.imshow("img", world)
cv2.waitKey(0)


