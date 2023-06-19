"""
File: blur.py
Name: Jason Lee
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: img, the image we desire to deal with
    :return: new_img, that is blurred
    """
    # Create a new blank image of the same size as the input image
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            red = 0
            green = 0
            blue = 0
            count = 0
            # For each pixel,sum up the red,green,and blue values of the pixel and its eight neighboring pixels
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    # the neighboring pixels are within the bounds of the input image
                    if 0 <= x + dx < img.width and 0 <= y + dy < img.height:
                        img_pixel = img.get_pixel(x+dx, y+dy)
                        red += img_pixel.red
                        green += img_pixel.green
                        blue += img_pixel.blue
                        count += 1
            # Divide each sum by the number of pixels we added together (count)
            new_img_pixel = new_img.get_pixel(x, y)
            new_img_pixel.red = red // count
            new_img_pixel.green = green // count
            new_img_pixel.blue = blue // count
    # return the output image
    return new_img


def main():
    """
     This file contains 1 image processing algorithm:
    blur
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
