#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from PIL import Image
import os

file = os.path.realpath(str(input("Enter image path: ")))
final_file_path = os.path.realpath(str(input("Enter final file path: ")))

if os.path.exists(final_file_path):
    erase = str(input(f"Erase {os.path.normpath(final_file_path)} ? (Y/N) :"))
    erase_ = True if erase.upper() == "Y" else False
    while not erase_:
        final_file_path = os.path.realpath(str(input("Enter new final file path: ")))
        if os.path.exists(final_file_path):
            erase = str(input(f"Erase {os.path.normpath(final_file_path)} ? (Y/N) :"))
            erase_ = True if erase.upper() == "Y" else False
        else:
            erase_ = True  # the file does not exist ;)

ascii_char = ' .:-=+*#%@'

with Image.open(file) as image:
    # cross product
    # x  50
    # y  y'
    # y' = 50y//x
    image = image.resize((50, (50 * image.height // image.width)))
    with open(final_file_path, "w", encoding="UTF-8") as final_file:
        for y in range(image.height):
            line = ''
            for x in range(image.width):
                # get pixel in RGB format
                pixel_rgb = image.getpixel((x, y))
                # grey level (between 0 and 255) is obtained by calculating the mean of each RGB color
                # (between 0 and 255 too)
                grey = sum(pixel_rgb) // len(pixel_rgb)
                # now we get the idx in our ascii_char by making a cross product
                idx = grey * 9 // 255
                # then we add it to our line
                line += ascii_char[idx] + " "  # we add 1 space : a char is more height than wide
            final_file.write(line + '\n')
            print(line)
    final_file.close()
