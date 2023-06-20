"""
File: babygraphics.py
Name: Jason Lee
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    width = CANVAS_WIDTH

    # Calculate the width of each section on the canvas
    section_width = width // len(YEARS)

    x_coordinate = year_index * section_width + GRAPH_MARGIN_SIZE

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Draw the top horizontal line at the margin position
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE)

    # Draw the bottom horizontal line at the margin position
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)

    # Draw the left vertical line at the margin position
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)

    # Draw vertical lines and year labels for each year
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    max_rank = MAX_RANK

    # Calculate the y-coordinate scale factor
    y_scale = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / max_rank

    for i in range(len(lookup_names)):
        name = lookup_names[i]
        name_ranks = name_data[name]

        # Plot the first data point for each name
        if str(YEARS[0]) in name_ranks:
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, 0) + TEXT_DX,
                               int(name_ranks[str(YEARS[0])]) * y_scale + GRAPH_MARGIN_SIZE,
                               text=f'{name} {name_ranks[str(YEARS[0])]}',
                               anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
        else:
            # If the first year rank is over 1000, plot an asterisk
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                               text=f'{name} *', anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

        for j in range(1, len(YEARS)):
            # Check if the current year exists in name_ranks(from 1910 to 2010) not over 1000
            if str(YEARS[j]) in name_ranks:
                rank = name_ranks[str(YEARS[j])]
                x = get_x_coordinate(CANVAS_WIDTH, j)
                y = int(name_ranks[str(YEARS[j])]) * y_scale + GRAPH_MARGIN_SIZE

                # Plot the data point for the current year
                canvas.create_text(x + TEXT_DX, y, text=f'{name} {name_ranks[str(YEARS[j])]}',
                                   anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

                # Check if the previous year not over 1000(current year rank and previous year rank both not over 1000)
                if str(YEARS[j-1]) in name_ranks:
                    prev_x = get_x_coordinate(CANVAS_WIDTH, j - 1)
                    prev_y = int(name_ranks[str(YEARS[j - 1])]) * y_scale + GRAPH_MARGIN_SIZE
                    canvas.create_line(prev_x, prev_y, x, y, fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)

                # current year rank not over 1000, previous year rank over 1000
                else:
                    prev_x = get_x_coordinate(CANVAS_WIDTH, j - 1)
                    prev_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    # Plot a line connecting the previous data point and the current data point
                    canvas.create_line(prev_x, prev_y, x, y, fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)

            # current year rank over 1000
            else:
                x = get_x_coordinate(CANVAS_WIDTH, j)
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                # current year rank over 1000, previous year rank not over 1000
                if str(YEARS[j - 1]) in name_ranks:
                    prev_rank = name_ranks[str(YEARS[j - 1])]
                    prev_x = get_x_coordinate(CANVAS_WIDTH, j - 1)
                    prev_y = int(name_ranks[str(YEARS[j - 1])]) * y_scale + GRAPH_MARGIN_SIZE
                    canvas.create_text(x + TEXT_DX, y, text=f'{name} *', anchor=tkinter.SW,
                                       fill=COLORS[i % len(COLORS)])
                    canvas.create_line(prev_x, prev_y, x, y, fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)
                # current year rank and previous year rank both over 1000
                else:
                    prev_x = get_x_coordinate(CANVAS_WIDTH, j-1)
                    prev_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(x + TEXT_DX, y, text=f'{name} *',
                                       anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
                    canvas.create_line(prev_x, prev_y, x, y, fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
