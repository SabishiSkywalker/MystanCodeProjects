"""
File: draw_line.py
Name: Jason Lee
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the circle
SIZE = 20
# Global variable
window = GWindow()  # create a window object
circle = None  # initialize the circle variable to None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_a_object)  # bind create_object function to the mouse click event


def create_a_object(mouse):
    """
    This function is called whenever the mouse is clicked on the window.
    It creates a circle on the first mouse click and a line on the second mouse click.
    """
    global circle  # use the global circle variable
    if circle is None:  # check if a circle has already been created
        # create a new circle object
        circle = GOval(SIZE, SIZE)
        # the circle object is hollow
        circle.filled = False
        # add the circle object to the window
        window.add(circle, mouse.x, mouse.y)
    else:
        # remove the existing circle from the window
        window.remove(circle)
        # create a new line object connecting the center of the circle to the mouse click location
        line = GLine(circle.x + SIZE / 2, circle.y + SIZE / 2, mouse.x, mouse.y)
        # add the line object to the window
        window.add(line)
        # set the circle variable back to None to indicate that the circle has been removed
        circle = None


if __name__ == "__main__":
    main()
