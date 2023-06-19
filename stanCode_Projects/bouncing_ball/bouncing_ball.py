"""
File: bouncing_ball.py
Name: Jason Lee
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
MAX_COUNT = 3

# Gate to prevent animation until the user clicks the mouse
start_animation = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    # Create a window and a ball
    window = GWindow(800, 500, title='bouncing_ball.py')
    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball)
    global start_animation
    onmouseclicked(click)
    vx = VX
    vy = 0
    count = 0
    while True:
        if start_animation:
            ball.move(vx, vy)
            # Check for collision with bottom wall
            if ball.y + SIZE > window.height:
                if vy > 0:
                    vy = -vy * REDUCE
            # Check for the ball is out of the right wall
            if ball.x + SIZE > window.width:
                vy = 0
                count += 1
                start_animation = False
                ball.x = START_X
                ball.y = START_Y
                window.add(ball, ball.x, ball.y)
            if count > MAX_COUNT:
                start_animation = False
                break
            vy += GRAVITY
        pause(DELAY)


# Mouse event to start the animation when the user clicks the mouse
def click(mouse):
    global start_animation
    start_animation = True


if __name__ == "__main__":
    main()
