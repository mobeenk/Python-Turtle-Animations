
#
# -------------------------------------------------

import turtle as t
import ball

screen = t.Screen()
screen.tracer(0)
t.delay(0)
t.speed(10)
t.hideturtle() # hide cursor
screen.listen()
t.onscreenclick(ball.creat_ball, btn=1)
screen.onkey(ball.toggle_move, 'space')
t.onscreenclick(ball.reset, btn=3)
while True:
    t.clear()
    ball.draw_edge()
    ball.move_balls()
    ball.draw_balls()
    screen.update()
t.done()
