import arcpy, sys

arcpy.env.workspace = "data/rastTester.gdb"
arcpy.env.overwriteoutput = True
substring = "*cover*"

rasts = arcpy.ListRasters(substring)

for rast in rasts:
    print(rast)
    fields = arcpy.ListFields(rast)
    for field in fields:
        print('\t' + field.name)