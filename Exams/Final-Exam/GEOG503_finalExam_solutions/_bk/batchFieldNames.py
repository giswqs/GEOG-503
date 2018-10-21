# batchFieldNames.py
# Purpose:  For rasters whose name contains a given substring,
#           print the raster names and their field names.
# Usage:  input_workspace substring
# Example: C:/gispy/data/ch11/rastTester.gdb COVER
import arcpy, sys

arcpy.env.workspace = sys.argv[1]
arcpy.env.overwriteoutput = True
substring = '*{0}*'.format(sys.argv[2])

rasts = arcpy.ListRasters(substring)

for rast in rasts:
    print rast
    fields = arcpy.ListFields(rast)
    for field in fields:
        print '\t' + field.name
