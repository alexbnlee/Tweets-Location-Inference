# Merge the whole polygons into one

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyrs = arcpy.mapping.ListLayers(df)
arcpy.Merge_management(lyrs, "Suburbs_MB_2016_AUS")
