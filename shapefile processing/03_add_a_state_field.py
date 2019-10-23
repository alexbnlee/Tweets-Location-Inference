# Before merging those polygons, we should point a specific field storing state info.
# Before doing this, atrribute window should be closed, or it won't work.

import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyrs = arcpy.mapping.ListLayers(df)
for lyr in lyrs:
    arcpy.AddField_management(lyr, "State", "TEXT")
  
# file name like "Suburbs_MB_2016_NSW"
# we want to get "NSW"

for lyr in lyrs:
    cursor = arcpy.UpdateCursor(lyr)
    fn = lyr.name
    for row in cursor:
        row.setValue("State", fn[fn.rfind("_")+1:])
        cursor.updateRow(row)
