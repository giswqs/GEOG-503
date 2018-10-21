__author__ = 'Qiusheng'

import arcpy
import os

workspace = r"C:\Geog503\data"
clip_fc = r"C:\Geog503\data\basin.shp"
output_dir = r"C:\Geog503\Results"

arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True
fc_list = arcpy.ListFeatureClasses()

desc = arcpy.Describe(clip_fc)
if desc.path == workspace:
    fc_list.remove(desc.file)

for fc in fc_list:
    out_fc = os.path.join(output_dir,fc)
    arcpy.Clip_analysis(fc,clip_fc,out_fc)

