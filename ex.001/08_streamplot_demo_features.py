# -*- coding: utf8 -*-
import numpy as np
import matplotlib.pyplot as plt

y, x = np.mgrid[-3:3:100j, -3:3:100j]
u = -1 - x**2 + y
v = 1 + x - y**2
speed = np.sqrt(u * u + v * v)

fig0, ax0 = plt.subplots()
strm = ax0.streamplot(x, y, u, v, color=u, linewidth=2, cmap=plt.cm.autumn)
fig0.colorbar(strm.lines)

fig1, (ax1, ax2) = plt.subplots(ncols=2)
ax1.streamplot(x, y, u, v, density=[0.5, 1])

lw = 5 * speed / speed.max()
ax2.streamplot(x, y, u, v, density=0.6, color='k', linewidth=lw)

plt.show()

#http://matplotlib.org/examples/images_contours_and_fields/streamplot_demo_features.html
#2016-9-13