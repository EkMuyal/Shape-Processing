Here both scripts are doing the same process (one with arguments and the other with just code)

The code delete all shapes that lide inside a polygon or are around a line (we need to set the buffer in grades).

the code delete_over.py is ready, you need to set the parameters editing the code


delete_over_func.py needs to be executed in the following way:

python delete_over_func.py test.shp town.shp line_final.shp 0.0045 my_experiment.shp

where:

- test.shp  is the file that contains all the polygons and you want to clean some of them
- town.shp is the shape that contains one or more polygons, all shapes inside those polygons are going to be erased
- line_final.shp is the shape that contain a line, the elements inside the buffer are going to be erased
- # the number is the buffer in grades
- my_experiment.shp is the name of the shapefile output

NOTE: I DID THE FUNCTION BUT I DID NOT PROBE IT, IF IT HAS SOME ERROS, I GUESS THOSE ARE VERY SIMPLE TO SOLVE