

# ======================================================================================================
# Simulation : Grand Bara land
# Code written by:
#   Ing. Nassim AM
#   Université.., France
# See Copyright Notice in COPYRIGHT
# HowTo in README.md
# ======================================================================================================

import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib import pyplot as plt
#import plotly.express as px


points=np.random.rand(200,2)
gb=Voronoi(points)


plt.scatter(points[:,0],points[:,1])
fig=voronoi_plot_2d(gb,show_points=0,show_vertices=0,line_width=2)
plt.savefig("Simulation.png")
plt.show()

