import fiona
import shapefile
import itertools
from shapely.geometry import shape, mapping, Polygon
import geopandas as gpd





def main(main_shape, polygon_shape, line_shape, buff_range ,name_output_shape):

    #load the data
    g1 = gpd.GeoDataFrame.from_file(main_shape) #shape ml prediction
    g2 = gpd.GeoDataFrame.from_file(polygon_shape) #shape of town
    g3 = gpd.GeoDataFrame.from_file(line_shape) #shape of duct


    print(len(g1))

    #the type of shape
    #aqui se puede ver que tipo de gometria se esta analizando
    #print(g3.geom_type) #LineString
    #print(g2.geom_type) #Polygon


    #delete the overlapping data / shapes and town or polygon
    data = []
    x = 0
    for index, pool in g1.iterrows():
        for index2, square in g2.iterrows():
            if pool['geometry'].intersects(square['geometry']) == True :
                g1.drop(index, inplace=True)

    #line duct / delete the overlapping data in a given buffer

    set_buffer = float(buff_range)

    for indexx, pool in g1.iterrows():
        for indexx2, line in g3.iterrows():
            #buffer
            if pool['geometry'].intersects(line['geometry'].buffer(set_buffer)) == True :
                    g1.drop(indexx, inplace=True)


    #length of the new polygon
    print(len(g1))

    g1.to_file(name_output_shape)

if __name__ == "__main__":

    #
    # example run : $ python delete_over_func.py test.shp town.shp line_final.shp 0.00345 my_experiment.shp
    #

	if len( sys.argv ) != 6:
		print("[ ERROR ] you must supply : main_shape_name, shape_of_the_polygons, shape_of_the_line, buffer_grades, and name_of_output")
		sys.exit( 1 )

	main(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])