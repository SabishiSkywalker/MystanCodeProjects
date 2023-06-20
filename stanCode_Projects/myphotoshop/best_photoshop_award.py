"""
File: best_photoshop_award.py
Name: Jason Lee
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.09

# Controls the upper bound for black pixel
BLACK_PIXEL = 150


def main():
    """
    創作理念：由於近期3/22即將上映捍衛任務4，想向John Wick致敬，頭上戴的粉紅色鴨舌帽印有捐血中心圖案，代表著熱血沸騰
    """
    fg = SimpleImage('image_contest/Jason.jpg')
    bg = SimpleImage('image_contest/gun.jpg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


def combine(bg, me):
    """
    : param1 bg: SimpleImage, the background image
    : param2 ma: SimpleImage, green screen figure image
    : return me: SimpleImage, the green screen pixels are replaced by pixels of background image
    """
    for y in range(bg.height):
        for x in range(bg.width):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red+pixel_me.blue+pixel_me.green)//3
            total = pixel_me.red+pixel_me.blue+pixel_me.green
            if pixel_me.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
