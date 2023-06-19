"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program implements the classic arcade game Breakout.
The game involves moving a paddle at the screen to bounce a ball and break bricks at the top of the screen.
The player has three lives and loses a life each time the ball falls off the bottom of the screen.
The game ends when the player breaks all the bricks or loses all their lives.

"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    lives = NUM_LIVES

    # Add the animation loop here!
    while lives > 0:
        num_brick = graphics.get_num_brick()
        if num_brick == 0:
            break
        if graphics.start_move:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            graphics.ball.move(dx, dy)
            graphics.handle_collision()
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                dx = graphics.change_x_direction()
            if graphics.ball.y <= 0:
                dy = graphics.change_y_direction()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                graphics.reset_ball()
                if lives > 0:
                    graphics.reset_ball()
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
