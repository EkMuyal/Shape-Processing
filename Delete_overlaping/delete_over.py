import fiona
import shapefile
import itertools
from shapely.geometry import shape, mapping, Polygon
import geopandas as gpd


#load the data
g1 = gpd.GeoDataFrame.from_file("prediccion-tif-completo-shard-1.shp") #shape ml prediction
g2 = gpd.GeoDataFrame.from_file("town.shp") #shape of town
g3 = gpd.GeoDataFrame.from_file("line_final.shp") #shape of duct


print(len(g1))

#the type of shape
#aqui se puede ver que tipo de gometria se esta analizando
#print(g3.geom_type) #LineString
#print(g2.geom_type) #Polygon


#delete the overlapping data / shapes and town or polygon
data = []
x = 0
for index, pool in g1.iterrows():
	for index2, town in g2.iterrows():
		if pool['geometry'].intersects(town['geometry']) == True :
			g1.drop(index, inplace=True)

#line duct / delete the overlapping data in a given buffer

set_buffer = 0.0005

for indexx, pool in g1.iterrows():
	for indexx2, line in g3.iterrows():
		#buffer
		if pool['geometry'].intersects(line['geometry'].buffer(set_buffer)) == True :
        		g1.drop(indexx, inplace=True)


#length of the new polygon
print(len(g1))

g1.to_file('intersection.shp')
