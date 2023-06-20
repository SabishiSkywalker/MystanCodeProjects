"""
File: stanCodoshop.py
Name: Jason Lee
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""
import math
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    # Calculate the distance between the pixel's RGB values and the average RGB values
    color_dist = math.sqrt((pixel.red-red)**2 + (pixel.green-green)**2 + (pixel.blue-blue)**2)
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # Initialize variables for sum of red, green, and blue values
    sum_red = 0
    sum_green = 0
    sum_blue = 0

    # Iterate over each pixel in the list and add its RGB values to the respective sum variables
    for pixel in pixels:
        sum_red += pixel.red
        sum_green += pixel.green
        sum_blue += pixel.blue

    # Calculate the average RGB values by dividing each sum by the number of pixels
    num_pixels = len(pixels)
    avg_red = sum_red // num_pixels
    avg_green = sum_green // num_pixels
    avg_blue = sum_blue // num_pixels

    # Return the average RGB values in a list
    return [avg_red, avg_green, avg_blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # Calculate the average red, green, and blue values of the pixels in the list
    sum_red = 0
    sum_green = 0
    sum_blue = 0

    for pixel in pixels:
        sum_red += pixel.red
        sum_green += pixel.green
        sum_blue += pixel.blue

    num_pixels = len(pixels)
    avg_red = sum_red // num_pixels
    avg_green = sum_green // num_pixels
    avg_blue = sum_blue // num_pixels

    # Initialize variables to store the best pixel and the smallest color distance found so far
    best_pixel = None
    smallest_dist = float('inf')

    # Iterate through each pixel in the list and calculate its color distance to the average RGB value
    for pixel in pixels:
        dist = get_pixel_dist(pixel, avg_red, avg_green, avg_blue)

        # Update the best pixel and smallest color distance if a pixel with smaller distance is found
        if dist < smallest_dist:
            smallest_dist = dist
            best_pixel = pixel

    # Return the pixel with the smallest color distance to the average RGB value
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    # get the dimensions of the images
    width = images[0].width
    height = images[0].height

    # create a new blank image to hold the result
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # loop over each pixel in the image
    for x in range(width):
        for y in range(height):
            # create a list to hold the pixels at this location from each input image
            pixels = []
            for image in images:
                pixels.append(image.get_pixel(x, y))
            # get the pixel with the closest color to the average of the input pixels
            best_pixel = get_best_pixel(pixels)
            # set the corresponding pixel in the result image to the color of the best pixel
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
    # ----- YOUR CODE ENDS HERE ----- #

    # display the resulting image and return it
    print("Displaying image!")
    result.show()
    return result


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()




