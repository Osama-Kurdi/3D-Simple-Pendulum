
# SIMPLE PENDULUM 3D

from vpython import *
from math import cos, radians
import time

o = 1
w0 = 3
x_max = 4
phi = 0
r = vector(0, 0, 0)
pos = vector(0, 0, 0)
helix_ = helix(pos=pos,
        axis=r, radius=0.5)

ball = sphere(pos=pos,
                radius=0.5, color=color.green)


label(pos=vector(110, 380, 0), pixel_pos=True, text='Made by MHD Usama Kurdi')

t = 0
while True:
    x = x_max * cos (w0*t + phi)
    helix_.axis = r
    ball.pos = r
    pos.y = -(x + x_max)
    r.y = -(x + x_max)
    t = time.perf_counter()
    
