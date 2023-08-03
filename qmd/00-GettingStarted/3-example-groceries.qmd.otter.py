











#| code-fold: true
%load_ext autoreload
%autoreload 2
%matplotlib inline
import matplotlib_inline
import matplotlib.pyplot as plt
import geopandas as gpd
import warnings
import geodatasets

import matplotlib.pyplot as plt

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

from ClimRR import set_plot_style, COLORS
set_plot_style()
from rich.console import Console as Console
from enrich.style import STYLES
from rich.theme import Theme

import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import box
import geodatasets

console = Console(theme=Theme(STYLES), log_path=False, markup=True)
chicago = gpd.read_file(geodatasets.get_path("geoda.chicago_commpop"))
groceries = gpd.read_file(geodatasets.get_path("geoda.groceries")).to_crs(chicago.crs)





































#| echo: false
#| code-fold: true
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(14, 6))
chicago.boundary.plot(ax=ax, color=COLORS['grey060'], linewidth=0.6, zorder=-1)
chicago.plot(ax=ax, alpha=0.0)
chicago.boundary.plot(ax=ax, color=COLORS['grey060'], linewidth=0.6, zorder=-1)
groceries.plot(ax=ax, color=COLORS['red'], zorder=1, marker='.', alpha=0.88)
ax.set_title("Grocery Stores in Chicago", fontsize=20)
ax.set_axis_off()
plt.tight_layout()




















import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import box
import geodatasets










import geodatasets
chicago = gpd.read_file(geodatasets.get_path("geoda.chicago_commpop"))
groceries = gpd.read_file(geodatasets.get_path("geoda.groceries")).to_crs(chicago.crs)





near_west_side = chicago[chicago["community"] == "NEAR WEST SIDE"]
lincoln_park = chicago[chicago["community"] == "LINCOLN PARK"]
logan_square = chicago[chicago["community"] == "LOGAN SQUARE"]





polygon = box(-87.8, 41.9, -87.5, 42)
poly_gdf = gpd.GeoDataFrame([1], geometry=[polygon], crs=chicago.crs)





fig, (ax1, ax2) = plt.subplots(figsize=(14, 6), ncols=2, sharey='col')
poly_gdf.boundary.plot(ax=ax1, color=COLORS['red'])
chicago.boundary.plot(ax=ax1, color=COLORS['grey060'], linewidth=0.6, zorder=-1)
# near_west_side.boundary.plot(ax=ax2, color=COLORS['red'])
# near_west_side.plot(ax=ax2, color=COLORS['green'], alpha=0.3)
# west_town.plot(ax=ax2, color=COLORS['green'], alpha=0.3)
chicago.plot(ax=ax1, alpha=0.4)
poly_gdf.boundary.plot(ax=ax2, color=COLORS['red'])
chicago.boundary.plot(ax=ax2, color=COLORS['grey060'], linewidth=0.6, zorder=-1)
groceries.plot(ax=ax2, color=COLORS['blue'], zorder=1, marker='.', alpha=0.66)
ax1.set_title("All Unclipped Chicago Communities", fontsize=20)
ax2.set_title("All Unclipped Groceries", fontsize=20)
ax1.set_axis_off()
ax2.set_axis_off()
plt.tight_layout()






















chicago_clipped = chicago.clip(polygon)
groceries_clipped = groceries.clip(polygon)
# plot the clipped data
fig, ax = plt.subplots(figsize=(14, 6), ncols=2)
ax0 = chicago_clipped.plot(ax=ax[0], color='C0', alpha=0.66)
ax0 = chicago.boundary.plot(ax=ax[0], color=COLORS['grey060'], zorder=-1, linewidth=0.6)
ax0 = poly_gdf.boundary.plot(ax=ax[0], color=COLORS['red'])

ax1 = groceries_clipped.plot(ax=ax[1], color='C1', alpha=0.66, zorder=10, marker='.')
# chicago.boundary.plot(ax=ax[1], color='#444444')
ax1 = chicago.boundary.plot(ax=ax[1], color=COLORS['grey060'], zorder=-1, linewidth=0.6)
ax1 = poly_gdf.boundary.plot(ax=ax[1], color=COLORS['red'])

ax0.set_title("Chicago Clipped", fontsize=20)
ax0.set_axis_off()
ax1.set_title("Groceries Clipped", fontsize=20)
ax1.set_axis_off()
plt.tight_layout()







fig, (ax1, ax2) = plt.subplots(figsize=(14, 6), ncols=2, sharey='col')
chicago.boundary.plot(ax=ax1, color=COLORS['grey060'], linewidth=0.6, zorder=-1)
near_west_side.boundary.plot(ax=ax2, color=COLORS['red'])
near_west_side.plot(ax=ax2, color=COLORS['green'], alpha=0.3)

logan_square.boundary.plot(ax=ax2, color=COLORS['red'])
logan_square.plot(ax=ax2, color=COLORS['green'], alpha=0.3)
# west_town.plot(ax=ax2, color=COLORS['green'], alpha=0.3)
chicago.plot(ax=ax1, alpha=0.4)
chicago.boundary.plot(ax=ax2, color=COLORS['grey060'], linewidth=0.6, zorder=-1)
groceries.plot(ax=ax2, color=COLORS['blue'], zorder=1, marker='.', alpha=0.66)
ax1.set_title("All Unclipped Chicago Communities", fontsize=20)
ax2.set_title("All Unclipped Groceries", fontsize=20)
ax1.set_axis_off()
ax2.set_axis_off()
plt.tight_layout()






groceries_west_side = groceries.clip(near_west_side)
fig, ax = plt.subplots(figsize=(14,6))
groceries_west_side.plot(ax=ax, color='C2', marker='.', alpha=0.6)
chicago.boundary.plot(ax=ax, color=COLORS['grey060'], linewidth=0.6, zorder=-1)
near_west_side.boundary.plot(ax=ax, color='#444444')
near_west_side.boundary.plot(ax=ax, color=COLORS['red'])
near_west_side.plot(ax=ax, color=COLORS['green'], alpha=0.3)
ax.set_title("Groceries in the Near West Side")
ax.set_axis_off()






groceries_logan_square = groceries.clip(logan_square)
fig, ax = plt.subplots(figsize=(14,6))
groceries_logan_square.plot(ax=ax, color='C2', marker='.', alpha=0.6)
chicago.boundary.plot(ax=ax, color=COLORS['grey060'], linewidth=0.6, zorder=-1)
logan_square.boundary.plot(ax=ax, color='#444444')
logan_square.boundary.plot(ax=ax, color=COLORS['red'])
logan_square.plot(ax=ax, color=COLORS['green'], alpha=0.3)
ax.set_title("Groceries in Logan Square")
ax.set_axis_off()






groceries_lp = groceries.clip(lincoln_park)
fig, ax = plt.subplots(figsize=(14,6))
groceries_lp.plot(ax=ax, color='C2')
chicago.boundary.plot(ax=ax, color=COLORS['grey060'], linewidth=0.6, zorder=-1)
lincoln_park.boundary.plot(ax=ax, color='#444444')
lincoln_park.boundary.plot(ax=ax, color=COLORS['red'])
lincoln_park.plot(ax=ax, color=COLORS['green'], alpha=0.3)
ax.set_title("Groceries in Lincoln Park")
ax.set_axis_off()
