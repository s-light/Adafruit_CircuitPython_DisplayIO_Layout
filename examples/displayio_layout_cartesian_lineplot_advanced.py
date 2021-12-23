# SPDX-FileCopyrightText: 2021 Stefan Krüger
#
# SPDX-License-Identifier: MIT
#############################
"""
This is a basic demonstration of a Cartesian widget for line-ploting
"""

import time
import random
import board
import displayio
from adafruit_displayio_layout.widgets.cartesian import Cartesian

# create the display on the PyPortal or Clue or PyBadge(for example)
display = board.DISPLAY
# otherwise change this to setup the display
# for display chip driver and pinout you have (e.g. ILI9341)

# pybadge display:  160x128
# Create a Cartesian widget
# https://circuitpython.readthedocs.io/projects/displayio-layout/en/latest/api.html#module-adafruit_displayio_layout.widgets.cartesian
my_plane = Cartesian(
    x=25,  # x position for the plane
    y=2,  # y plane position
    width=130,  # display width
    height=105,  # display height
    xrange=(0, 10),  # x range
    yrange=(0, 10),  # y range
)

my_group = displayio.Group()
my_group.append(my_plane)
display.show(my_group)  # add high level Group to the display

data = [
    # (0, 0),  # we do this point manually - so we have no wait...
    (1, 1),
    (2, 1),
    (2, 2),
    (3, 3),
    (4, 3),
    (4, 4),
    (5, 5),
    (6, 5),
    (6, 6),
    (7, 7),
    (8, 7),
    (8, 8),
    (9, 9),
    (10, 9),
    (10, 10),
]

print("examples/displayio_layout_cartesian_lineplot.py")


print("draw lines")
# first point without a wait.
my_plane.add_plot_line(0, 0)
for x, y in data:
    my_plane.add_plot_line(x, y)
    time.sleep(0.1)


print("clear all lines.")
my_plane.clear_plot_lines()

print("change x & y range")
my_plane.xrange = (15, 65)
my_plane.yrange = (14, 20)

print("draw lines")
my_plane.add_plot_line(my_plane.xrange[0], my_plane.yrange[0])
for x in range(*my_plane.xrange):
    my_plane.add_plot_line(x, random.randint(*my_plane.yrange))
    time.sleep(0.1)

print("done.")
while True:
    pass
