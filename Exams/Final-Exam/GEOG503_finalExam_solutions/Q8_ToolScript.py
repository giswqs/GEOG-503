import arcpy, traceback

fc = arcpy.GetParameterAsText(0)
field = arcpy.GetParameterAsText(1)
output = arcpy.GetParameterAsText(2)

try:
    if arcpy.Exists(output):
        arcpy.Delete_management(output)

    arcpy.Copy_management(fc, output)
    arcpy.AddMessage('Copied {0} to {1}'.format(fc, output))
    with arcpy.da.UpdateCursor(output, [field]) as cursor:
        for row in cursor:
            row[0] = row[0].upper()
            cursor.updateRow(row)
    arcpy.AddMessage('Modified {0}'.format(output))
    del cursor
except:
    arcpy.AddMessage('An error occurred.')
    traceback.print_exc()
