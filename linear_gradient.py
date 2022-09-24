import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 1
f1 = float (0.5 / size)
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [0, 128, 255]
color2 = [255, 128, 0]
v = f1

for j in range(size):

    for i in range(size):

        r = lerp(color1[0], color2[0], v)
        g = lerp(color1[1], color2[1], v)
        b = lerp(color1[2], color2[2], v)
        image[i,j,:] = [r, g, b]
        v = v + f1

    v = f1 * (j+1)

plt.figure(1)
plt.imshow(image)
plt.show()
