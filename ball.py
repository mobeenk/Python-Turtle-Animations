
#
# -------------------------------------------------
import random
import turtle as t
import math




def move_balls():
    # this function moves the ball with the equation [x,y] + [vel_x,vel_y].
    # it also makes sure the balles do not go beyond the box edges
    # To ensure the balles are inside, the vel_x and vel_y is multiplied by -1 if the ball excedes the boundaries.
    width = Ball.screen_width + Ball.ball_radious
    negative_width = (Ball.screen_width + Ball.ball_radious) * -1


    if Ball.move_flag:
        for i in Ball.list_of_balls:
            # bottom
            if i.y <= negative_width <= i.x :  # or i.x < negative_width
                if i.x < 0:
                    i.setVelY(i.getVelY() * -1)
                    i.y += Ball.getVelY(self=i)
                else:

                    i.setVelY(i.getVelY() * -1)
                    i.y += Ball.getVelY(self=i)


                print('bottom(', i.x, ',', i.y, ')')
            # top
            elif i.y >= width >= i.x :

                if i.x < 0:
                    i.setVelY(i.getVelY() * -1)
                    i.y += Ball.getVelY(self=i)
                else:

                    i.setVelY(i.getVelY() * -1)
                    i.y += Ball.getVelY(self=i)
            # left
            elif i.x <= negative_width <= i.y :

                if i.y < 0:
                    i.setVelX(i.getVelX() * -1)
                    i.x += Ball.getVelX(self=i)
                else:

                    i.setVelX(i.getVelX() * -1)
                    i.x += Ball.getVelX(self=i)
                print('left(', (i.x) * 1, ',', i.y, ')')



                print('top(', (i.x), ',', i.y, ')')
            elif i.x > width > i.y :
                # right
                if i.y < 0:
                    i.setVelX(i.getVelX() * -1)
                    i.x += Ball.getVelX(self=i)
                else:

                    i.setVelX(i.getVelX() * -1)
                    i.x += Ball.getVelX(self=i)



                print('right(', i.x, ',', i.y, ')')
            elif negative_width < i.x < width and negative_width < i.y < width :

                print('normal movement(', i.x, ',', i.y, ')')

                i.x += Ball.getVelX(self=i)
                i.y += Ball.getVelY(self=i)


def creat_ball(x, y):
    # This function creates the ball
    # The ball is created only if the mouse click was inside the box.
    # otherwise nothing happens.
    width = Ball.screen_width + Ball.ball_radious
    negative_width = (Ball.screen_width + Ball.ball_radious) * -1

    if negative_width < x < width and negative_width < y < width:
        Ball.list_of_balls.append(
            Ball(x, y)
        )
    else:
        print('outside')


def toggle_move():
    # This function stops the ball from moving if the key "space" is pressed.
    # The balls move again if "space" is pressed again and so on.
    Ball.move_flag = not Ball.move_flag


# ---------------------------------------------------------------------
# Don't change the code below
class Ball:
    # This is the ball class
    list_of_balls = []  # This is a list containing all balls object
    screen_width = 300  # The is the width of the box
    ball_radious = 10  # This is the radious of the ball
    move_flag = True  # this is the ball moving flag. If it is True, the balls move. If it is Flase, the balls stop.

    def __init__(self, x, y):
        self.x = x  # The ball x location
        self.y = y  # The ball y location
        self.vel_x = random.uniform(-2, 2)  # The ball x velocity
        self.vel_y = random.uniform(-2, 2)  # The ball y velocity
        self.color = (
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1)
        )  # The ball color created randomly

    def getVelX(self):
        return self.vel_x

    def getVelY(self):
        return self.vel_y

    def setVelX(self, newX):
        self.vel_x = newX

    def setVelY(self, newY):
        self.vel_y = newY


def draw_balls():
    # This is the turtle code to draw the ball
    for i in Ball.list_of_balls:
        t.penup()
        t.goto(i.x, i.y - Ball.ball_radious)
        t.color(i.color)
        t.pendown()
        t.begin_fill()
        t.circle(Ball.ball_radious)
        t.end_fill()
        t.color('black')


def draw_edge():
    # This is the turtle code to draw the edges of the box
    width = Ball.screen_width + Ball.ball_radious
    t.penup()
    t.goto(-width, -width)
    t.pendown()
    t.goto(width, -width)  # bottom left starts , and go right first line
    t.goto(width, width)  # go up
    t.goto(-width, width)  # left
    t.goto(-width, -width)  # down
    t.penup()


def reset(x, y):
    Ball.list_of_balls.clear()
