# loopGetCount.py
# Purpose:      Get the record count for each shapefile in
#               whose name contain the substring 'out', case-insensitive
# Input:        directory_path
# Example:      C:/gispy/data/ch10/archive

import arcpy, os, sys

path = sys.argv[1]
names = os.listdir(path)
arcpy.env.workspace = path
substring = 'out'

for name in names:
    # If the name has the search word (non-case-sensitive) & is a shapefile,...
    if substring in name.lower() and name.endswith('.shp'):
        count = arcpy.GetCount_management(name)
        print '{0} has {1} entries.'.format(name, count.getOutput(0))
