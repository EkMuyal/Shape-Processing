import fiona
from shapely.ops import cascaded_union
from shapely.geometry import shape, mapping
from tqdm import tqdm

with fiona.open('prediccion-con-desfase-shard-1.shp', 'r') as ds_in:
	crs = ds_in.crs
	drv = ds_in.driver


	def geometry_filter(shp):
		if shape(shp['geometry']).is_valid == False:
			shp['geometry'] = shape(shp['geometry']).buffer(0)
		return shp

	filtered = map(geometry_filter, list(ds_in))


	print(len(filtered))

	geoms = [shape(x["geometry"]) for x in tqdm(filtered)]
	dissolved = cascaded_union(geoms)

	print("------------------------------------")
	schema = {
	"geometry": "Polygon",
	"properties": {"id": "int"}
	}

	print("salio de la lectura")

with fiona.open('out_diss', 'w', driver=drv, schema=schema, crs=crs) as ds_dst:
	print("entro a la escritura")
	for i,g in tqdm(enumerate(dissolved)):
		ds_dst.write({"geometry": mapping(g), "properties": {"id": i}})

	print("xxxxxxxxxxxxxxxxxxxxxxxxxx")
#		ds_dst.close()

#	ds_in.close()
