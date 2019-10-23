# Merge polygons with the same attribute of "SA2_NAME16".

import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyrs = arcpy.mapping.ListLayers(df)
for lyr in lyrs:
    arcpy.Dissolve_management(lyr, "Dissolve_" + lyr.name, 'SA2_NAME16', '#', 'MULTI_PART', 'DISSOLVE_LINES')   
