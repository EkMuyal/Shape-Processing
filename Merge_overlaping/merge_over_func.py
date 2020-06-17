import fiona
import os, sys
from shapely.ops import cascaded_union
from shapely.geometry import shape, mapping
from tqdm import tqdm

def main(file_to_process, out_dir):

	with fiona.open(file_to_process, 'r') as ds_in:
		crs = ds_in.crs
		drv = ds_in.driver


		def geometry_filter(shp):
			if shape(shp['geometry']).is_valid == False:
				shp['geometry'] = shape(shp['geometry']).buffer(0)
			return shp

		filtered = map(geometry_filter, list(ds_in))


		#print(len(filtered))

		geoms = [shape(x["geometry"]) for x in tqdm(filtered)]
		dissolved = cascaded_union(geoms)

		print("------------------------------------")
		schema = {
		"geometry": "Polygon",
		"properties": {"id": "int"}
		}

		print("salio de la lectura")

	with fiona.open(out_dir, 'w', driver=drv, schema=schema, crs=crs) as ds_dst:
		print("entro a la escritura")
		for i,g in tqdm(enumerate(dissolved)):
			ds_dst.write({"geometry": mapping(g), "properties": {"id": i}})

		print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
#		ds_dst.close()

#	ds_in.close()
if __name__ == "__main__":

    #
    # example run : $ python merge_over_func.py <full-path><output-shapefile-name>.shp output_dir
    #

	if len( sys.argv ) != 3:
		print("[ ERROR ] you must supply a shape file name and out dir: file_to_process.shp out_dir")
		sys.exit( 1 )

	main(sys.argv[1],sys.argv[2])
