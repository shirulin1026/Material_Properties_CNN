import os
from PIL import Image

dire = "DEEPstruc"

min_x = 9999
min_y = 9999
avg_x = 0
avg_y = 0
avg_ratio = 0
n = len(os.listdir(dire))


for path in os.listdir(dire):
    image = Image.open(dire + "/" + path)

    x, y = image.size

    if x < min_x:
        min_x = x

    if y < min_y:
        min_y = y

    avg_x += x
    avg_y += y
    avg_ratio += (x/y) /n

avg_x /= n
avg_y /= n


print(min_x, min_y, avg_x, avg_y, avg_ratio)