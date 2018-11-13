import random
import csv
import PIL
from PIL import ImageColor
from PIL import Image

with open('elevation_small.txt', 'r') as word_file:
    elevation_data = [line.strip('\n').split() for line in word_file]

elevation_ints = [[int(num) for num in line] for line in elevation_data]

"""
This converts all numbers into integers.
"""

def get_maximum_elevation(list):

    max_numbers_list = [max(num) for num in list]
    max_elevation = max(max_numbers_list)
    return max_elevation


max_elevation = get_maximum_elevation(elevation_ints)
print(max_elevation)

"""
This finds the maximum number in the entire data set.
"""


def get_minimum_elevation(list):

    min_numbers_list = [min(num) for num in list]
    min_elevation = min(min_numbers_list)
    return min_elevation


min_elevation = get_minimum_elevation(elevation_ints)
print(min_elevation)

"""
This finds the minimum number in the entire data set.
"""
RGB_values = [[int((num - min_elevation)/(max_elevation - min_elevation) * 255)
               for num in line] for line in elevation_ints]

"""
This converts all numbers into values that can be read to create color on the map.
"""

image = Image.new("RGB", (600, 600))
for y, row in enumerate(RGB_values):
    for x, num in enumerate(row):
        image.putpixel((x, y), (num, num, num))
        image.putpixel((x, 250), (218, 112, 214))
image.save("map_image.png")
image.show("map_image.png")

"""
This creates the image using the converted elevation values.  
"""
