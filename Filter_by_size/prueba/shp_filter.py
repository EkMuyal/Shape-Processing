# coding=utf-8
import numpy as np
import geopandas as gpd
import fiona
import os


#definir los limites para el filtro
#metros cuadrados
maxf = 520.

minf = 10.

#directorios
dir_in = "/home/camilo_delahoz/shp_filter/prueba"
dir_out = "/home/camilo_delahoz/shp_filter/prueba/filtered"

if not os.path.exists(dir_out):
    os.makedirs(dir_out)



i = 1
for filename in os.listdir(dir_in):
	if filename.endswith(".shp"):
		shape = gpd.read_file(filename).to_crs(epsg=3116)
		print(filename)
		print("tamano del shape de entrada", shape.shape)
		#aplicar las mascaras de area
		mask1 = shape.area > minf
		mask2 = shape.area < maxf
		#filtrar el elemento
		selected_polygons = shape.loc[mask1]
		selected_polygons =  selected_polygons.loc[mask2]
		#resultados
		print("tamano del shape de salida", selected_polygons.shape)
		a,b = selected_polygons.shape
		if a > 0:
			print( str(i)+ ".shp")		#guardar en otro directorio
			selected_polygons.to_file(dir_out+"/"+ str(i) + ".shp")
		i = i+1
#mask = shape.area > 10.  # metres squared

#selected_polygons = shape.loc[mask]

#print("tamaño del shape de salida")
#print(selected_polygons.shape)


#selected_polygons.to_file('filtered_2.shp')
