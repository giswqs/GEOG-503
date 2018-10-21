# updateUPPER.py
# Purpose: Create a copy and change the input field values to uppercase.
# Usage: input_table field_name
# Example: C:/gispy/data/ch17/park.shp COVER
import arcpy, os, sys, traceback

fc = sys.argv[1]
field = sys.argv[2]

output = 'C:/gispy/scratch/' + os.path.basename(fc)
try:
    if arcpy.Exists(output):
        arcpy.Delete_management(output)

    arcpy.Copy_management(fc, output)
    print 'Copied {0} to {1}'.format(fc, output)
    with arcpy.da.UpdateCursor(output, [field]) as cursor:
        for row in cursor:
            row[0] = row[0].upper()
            cursor.updateRow(row)
    print 'Modified {0}'.format(output)
    del cursor
except:
    print 'An error occurred.'
    traceback.print_exc()
    del cursor
