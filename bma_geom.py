import math

def BMA_regular_polygon_vertices(n, radius, center=(0,0), heading=0.0):
    cx, cy = center
    a = 2*math.pi/n
    h = math.radians(heading)
    return [(cx + radius*math.cos(h + i*a), cy + radius*math.sin(h + i*a)) for i in range(n)]

def BMA_regular_polygon_side_length(n, radius):
    return 2*radius*math.sin(math.pi/n)

def BMA_regular_polygon_perimeter(n, radius):
    return n*BMA_regular_polygon_side_length(n, radius)

def BMA_regular_polygon_area(n, radius):
    return 0.5*n*(radius**2)*math.sin(2*math.pi/n)

def BMA_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)

def BMA_rotate_point(p, angle_deg, origin=(0,0)):
    x, y = p
    ox, oy = origin
    t = math.radians(angle_deg)
    cx = ox + (x-ox)*math.cos(t) - (y-oy)*math.sin(t)
    cy = oy + (x-ox)*math.sin(t) + (y-oy)*math.cos(t)
    return (cx, cy)