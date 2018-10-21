import arcpy, os, sys, traceback

fc = "data/park.shp"
field = "COVER"
output = 'results/' + os.path.basename(fc)

try:
    if arcpy.Exists(output):
        arcpy.Delete_management(output)

    arcpy.Copy_management(fc, output)
    print('Copied {0} to {1}'.format(fc, output))
    with arcpy.da.UpdateCursor(output, [field]) as cursor:
        for row in cursor:
            row[0] = row[0].upper()
            cursor.updateRow(row)
    print('Modified {0}'.format(output))
    del cursor
except:
    print('An error occurred.')
    traceback.print_exc()
    # del cursor
