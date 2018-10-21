__author__ = 'Qiusheng'

import arcpy
import os

workspace = arcpy.GetParameterAsText(0)
clip_fc = arcpy.GetParameterAsText(1)
output_dir = arcpy.GetParameterAsText(2)

arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True
fc_list = arcpy.ListFeatureClasses()

desc = arcpy.Describe(clip_fc)
if desc.path == workspace:
    fc_list.remove(desc.file)

if arcpy.Exists(output_dir) == False:
    arcpy.CreateFolder_management(os.path.split(output_dir)[0],os.path.split(output_dir)[1])

for fc in fc_list:
    out_fc = os.path.join(output_dir,fc)
    arcpy.Clip_analysis(fc,clip_fc,out_fc)

