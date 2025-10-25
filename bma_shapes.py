import random
from bma_geom import BMA_regular_polygon_vertices


class BMAFigure:
    def __init__(self, t):
        self.t = t
        self.x = 0
        self.y = 0
        self.heading = 0.0
        self.color = (0, 0, 0)
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def rotate(self, d):
        self.heading = (self.heading + d) % 360
    def random_color(self):
        self.color = (random.randrange(0,256), random.randrange(0,256), random.randrange(0,256))

class BMAPolygon(BMAFigure):
    def __init__(self, t, n=5, radius=100):
        super().__init__(t)
        self.n = max(3, int(n))
        self.radius = max(10, int(radius))
        self.random_color()
    def change_sides(self, dn):
        self.n = max(3, self.n + dn)
    def change_radius(self, dr):
        self.radius = max(10, self.radius + dr)
    def draw(self):
        vs = BMA_regular_polygon_vertices(self.n, self.radius, center=(self.x, self.y), heading=self.heading)
        self.t.penup()
        if not vs: 
            return
        self.t.goto(vs[0][0], vs[0][1])
        self.t.pendown()
        self.t.pencolor(self.color)
        for v in vs[1:]:
            self.t.goto(v[0], v[1])
        self.t.goto(vs[0][0], vs[0][1])

class BMAState:
    def __init__(self, draw_t, info_t):
        self.figure = BMAPolygon(draw_t, n=5, radius=100)
        self.show_info = True
        info_t.hideturtle()
        draw_t.hideturtle()
        draw_t.speed(0)