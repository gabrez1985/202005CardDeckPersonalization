from PIL import Image, ImageOps, ImageColor
import os
import sys


def open_image(path):
    newImage = Image.open(path)
    return newImage


def save_image(image, path):
    image.save(path, 'png')


def create_image(i, j, color=(255, 255, 255, 255)):
    image = Image.new("RGBA", (i, j), color)
    return image


def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
        return None
    pixel = image.getpixel((i, j))
    return pixel


nuevaimagen = create_image(150, 200, (0, 0, 0, 0))
save_image(nuevaimagen, 'Imagenes/nuevaimagenprueba.png')


# cambia del color blanco de un fondo a un nuevo color que se debe definir
def cambiarcolorfondo(image, color=(255, 255, 255, 255)):

    width, height = image.size

    new = create_image(width, height)
    pixels = new.load()

    for i in range(width):
        for j in range(height):
            pixel = get_pixel(image, i, j)
            # print(pixel)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            alpha = pixel[3]

            if red > 150 and green > 150 and blue > 150 and alpha > 150:
                pixels[i, j] = color
            else:
                pixels[i, j] = (0, 0, 0, 255)

    return new
