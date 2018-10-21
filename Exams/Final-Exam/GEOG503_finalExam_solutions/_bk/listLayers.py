# listLayers.py
# Purpose: Print each names of layer in each data frame.
# Usage: fullpath_mxd_filename
# Example input: C:/gispy/data/ch24/maps/states.mxd

import arcpy, sys
mapName = sys.argv[1]
mxd = arcpy.mapping.MapDocument(mapName)

# Get a list of data frame objects.
dfs = arcpy.mapping.ListDataFrames(mxd)
print 'Map: {0}\n'.format(mxd.filePath)

# Loop through data frames.
for i, df in enumerate(dfs):
    print 'Frame ' + str(i) + ': ' + df.name
    # Get a list of layer objects in the current dataframe.
    layers = arcpy.mapping.ListLayers(mxd, '*', df)
    # Loop through layers.
    for j, layer in enumerate(layers):
        print '\t Layer ' + str(j) + ": " + layer.name + ' ' + layer.dataSource

del mxd
