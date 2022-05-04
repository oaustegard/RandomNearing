# %% Adapted from https://ocefpaf.github.io/python4oceanographers/blog/2015/08/03/fiona_gpx/
import geopandas as gpd
import fiona
from shapely.geometry import shape
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.io.img_tiles as cimgt


# open the shapefile using fiona
fname = '/Users/austegard/Downloads/Parkwood_1_Randomnearing.gpx'
layer = fiona.open(fname, layer='tracks')
# These files only have a single layer, so we can use `layer[0]`
geom = layer[0]
(x0, y0, x1, y1) = layer.bounds #gets bounding points as x=long, y=lat
data = {'type': 'MultiLineString',
        'coordinates': geom['geometry']['coordinates']}

shp = shape(data)
# %%
def make_map(projection=ccrs.PlateCarree()):
    fig, ax = plt.subplots(figsize=(9, 13), subplot_kw=dict(projection=projection))
    gl = ax.gridlines(draw_labels=True)
    gl.top_labels = gl.right_labels = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    return fig, ax


request = cimgt.OSM()
fig, ax = make_map(projection=request.crs)
ax.set_extent([x0, x1, y0, y1]) #sets bounding x,y ranges -- note difference in order betwen this and fiona.layer.bounds
img = ax.add_image(request, 15) #TODO: #1 derive appropriate zoom level from bounds
s = ax.add_geometries(shp, ccrs.PlateCarree(),
                      facecolor='none',
                      edgecolor='blue',
                      linewidth=1)
# %%
