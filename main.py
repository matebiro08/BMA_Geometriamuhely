import turtle
import random
from bma_shapes import BMAPolygon, BMAState
from bma_geom import BMA_regular_polygon_area, BMA_regular_polygon_perimeter

screen = turtle.Screen()
screen.title("BMA Geometriaműhely")
screen.bgcolor("white")
turtle.colormode(255)
turtle.tracer(0, 0)

draw_t = turtle.Turtle(visible=False)
info_t = turtle.Turtle(visible=False)
draw_t.pensize(5)

state = BMAState(draw_t, info_t)

def BMA_redraw():
    draw_t.clear()
    info_t.clear()
    state.figure.draw()
    if state.show_info:
        a = BMA_regular_polygon_area(state.figure.n, state.figure.radius)
        p = BMA_regular_polygon_perimeter(state.figure.n, state.figure.radius)
        info_t.penup()
        info_t.goto(-screen.window_width()//2 + 20, screen.window_height()//2 - 40)
        info_t.write(f"n={state.figure.n}  R={state.figure.radius}  Terület≈{a:.2f}  Kerület≈{p:.2f}", font=("Arial", 12, "normal"))
    turtle.update()

def BMA_new_polygon():
    state.figure = BMAPolygon(draw_t, n=random.randrange(3, 10), radius=random.randrange(40, 140))
    BMA_redraw()

def BMA_rotate_left():
    state.figure.rotate(15)
    BMA_redraw()

def BMA_rotate_right():
    state.figure.rotate(-15)
    BMA_redraw()

def BMA_move_up():
    state.figure.move(0, 20)
    BMA_redraw()

def BMA_move_down():
    state.figure.move(0, -20)
    BMA_redraw()

def BMA_move_left():
    state.figure.move(-20, 0)
    BMA_redraw()

def BMA_move_right():
    state.figure.move(20, 0)
    BMA_redraw()

def BMA_color():
    state.figure.random_color()
    BMA_redraw()

def BMA_inc_sides():
    state.figure.change_sides(1)
    BMA_redraw()

def BMA_dec_sides():
    state.figure.change_sides(-1)
    BMA_redraw()

def BMA_inc_radius():
    state.figure.change_radius(10)
    BMA_redraw()

def BMA_dec_radius():
    state.figure.change_radius(-10)
    BMA_redraw()

def BMA_toggle_info():
    state.show_info = not state.show_info
    BMA_redraw()

def BMA_thick_up():
    draw_t.pensize(draw_t.pensize() + 1)
    BMA_redraw()

def BMA_thick_down():
    w = max(1, draw_t.pensize() - 1)
    draw_t.pensize(w)
    BMA_redraw()


def BMA_quit():
    turtle.bye()

state.figure.draw()
turtle.update()

screen.listen()
screen.onkey(BMA_new_polygon, "n")
screen.onkey(BMA_rotate_left, "f")
screen.onkey(BMA_rotate_right, "g")
screen.onkey(BMA_move_up, "Up")
screen.onkey(BMA_move_down, "Down")
screen.onkey(BMA_move_left, "Left")
screen.onkey(BMA_move_right, "Right")
screen.onkey(BMA_color, "c")
screen.onkey(BMA_inc_sides, "s")
screen.onkey(BMA_dec_sides, "a")
screen.onkey(BMA_inc_radius, "x")
screen.onkey(BMA_dec_radius, "z")
screen.onkey(BMA_toggle_info, "i")
screen.onkey(BMA_quit, "Escape")
screen.onkey(BMA_thick_up, "k")
screen.onkey(BMA_thick_down, "j")

turtle.mainloop()