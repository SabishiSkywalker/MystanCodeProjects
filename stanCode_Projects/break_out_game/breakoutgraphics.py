"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self._paddle = GRect(width=paddle_width, height=paddle_height,
                             x=(window_width-paddle_width)//2, y=window_height-paddle_offset)
        self._paddle_offset = paddle_offset
        self._paddle.filled = True
        self.window.add(self._paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius)//2,
                          y=(window_height-ball_radius)//2)
        self.ball_radius = ball_radius
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.start_move = False
        onmouseclicked(self.ball_move)
        onmousemoved(self.move_paddle)

        # Initialize collision
        self.collided = False

        # Draw bricks
        brick_counter = 0
        for row in range(brick_rows):
            for col in range(brick_cols):
                x = col*(brick_width + brick_spacing)
                y = row*(brick_height + brick_spacing) + brick_offset
                brick = GRect(width=brick_width, height=brick_height, x=x, y=y)
                brick.filled = True
                if row < 2:
                    brick.fill_color = 'red'
                elif 2 <= row < 4:
                    brick.fill_color = 'orange'
                elif 4 <= row < 6:
                    brick.fill_color = 'yellow'
                elif 6 <= row < 8:
                    brick.fill_color = 'green'
                elif 8 <= row < 10:
                    brick.fill_color = 'blue'
                self.window.add(brick)
                brick_counter += 1
        self.__num_brick = brick_counter

    def move_paddle(self, mouse):
        """
        Move the paddle to follow the mouse position.
        """
        if self._paddle.width / 2 < mouse.x < self.window.width - self._paddle.width / 2:
            self._paddle.x = mouse.x - self._paddle.width // 2
        elif mouse.x < self._paddle.width / 2:
            self._paddle.x = 0
        else:
            self._paddle.x = self.window.width - self._paddle.width

    def ball_move(self, event):
        if not self.start_move:
            self.start_move = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def reset_ball(self):
        # check if ball goes beyond the bottom edge of the window
        self.__dx = 0
        self.__dy = 0
        self.ball.x = (self.window.width - self.ball_radius)//2
        self.ball.y = (self.window.height - self.ball_radius)//2
        self.start_move = False

    def handle_collision(self):
        # Check for collisions at all four corners of the ball
        for x in range(int(self.ball.x), int(self.ball.x + self.ball.width + 1), self.ball.width):
            for y in range(int(self.ball.y), int(self.ball.y + self.ball.height + 1), self.ball.height):
                # Check if there's an object at the current corner
                obj = self.window.get_object_at(x, y)
                if obj is not None:
                    # Handle collision with the paddle
                    if obj is self._paddle:
                        # Check for collision with the paddle
                        if self.__dy > 0:
                            self.__dy = -self.__dy
                            return
                    # Handle collision with a brick
                    elif obj is not self._paddle:
                        # Remove the brick from the window
                        self.window.remove(obj)
                        # Update the number of bricks
                        self.__num_brick -= 1
                        # Reverse the y direction of the ball
                        self.__dy = -self.__dy
                        return

    def get_dx(self):
        """
        Returns the value of the horizontal velocity of the ball.
        """
        return self.__dx

    def get_dy(self):
        """
        Returns the value of the vertical velocity of the ball.
        """
        return self.__dy

    def get_num_brick(self):
        """
         Returns the value of the number of the brick.
        """
        return self.__num_brick

    def change_x_direction(self):
        self.__dx = -self.__dx
        return self.__dx

    def change_y_direction(self):
        self.__dy = -self.__dy
        return self.__dy

