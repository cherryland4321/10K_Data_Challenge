# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 14:33:35 2022

@author: erick
"""

import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import folium
from geopandas import GeoDataFrame

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
df_map = gpd.GeoDataFrame.from_file("19mun.shp")

data = pd.read_csv("Datos_Final.csv") 

new_map = pd.merge(df_map, data, left_index=True, right_index=True)
fig, ax = plt.subplots(1, 1,figsize=(12, 12))

#new_map.apply(lambda x: ax.annotate(text=x.Municipio, xy=x.geometry.centroid.coords[0], ha='center', fontsize=5),axis=1);

ax = new_map.plot(column="% Sin Agua Entubada (Acarreo)", ax=ax, edgecolor='k', legend=True) 
ax.set_axis_off()
fig.suptitle("% Sin Agua Entubada (Acarreo)")
plt.show()

correlacion = data["IDH"].corr(data["% Sin Agua Entubada (Acarreo)"])
print(correlacion)

outfp = r"C:\Users\erick\OneDrive\Escritorio\Proyecto_Agua\base_map.html"
new_map = new_map.rename(columns={c:str(c) for c in new_map.columns})
m = new_map.explore(min_zoom = -100)
#m = folium.Map(zoom_start = 18, max_zoom = 18)
#new_map.explore(m=m)
#world.explore(m=m)
#cities.explore(m=m)

m.save(outfp)
