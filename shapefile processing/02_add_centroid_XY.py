# After using the "Add Geometry Attributes" tool, we should close shp files and add them again and will see the results. 
# (Sometimes it can show directly, WTF!!!)
# Don't show attributes during processing.

import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyrs = arcpy.mapping.ListLayers(df)
for lyr in lyrs:
    arcpy.AddGeometryAttributes_management(lyr, "CENTROID")
