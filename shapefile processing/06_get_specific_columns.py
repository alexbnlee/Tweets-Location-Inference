# based on pandas lib.

>>> df = pd.read_csv(r"D:\Twitter Data\Data\test\2.csv")
>>> df.head()
       XCoord     YCoord     ...     STATE  SHAPE_AREA
0  117.899601 -35.008360     ...        WA    0.003012
1  118.207172 -34.718972     ...        WA    0.394533
2  115.865812 -31.834866     ...        WA    0.000638
3  115.677976 -31.600241     ...        WA    0.003104
4  115.836085 -32.019166     ...        WA    0.000518
 
[5 rows x 7 columns]
>>> df.columns
Index(['XCoord', 'YCoord', 'SA2_NAME16', 'CENTROID_X', 'CENTROID_Y', 'STATE',
       'SHAPE_AREA'],
      dtype='object')
>>> df1 = df[['SA2_NAME16', 'CENTROID_X', 'CENTROID_Y', 'STATE', 'SHAPE_AREA']]
>>> df1.columns
Index(['SA2_NAME16', 'CENTROID_X', 'CENTROID_Y', 'STATE', 'SHAPE_AREA'], dtype='object')
>>> df1.head()
                      SA2_NAME16  CENTROID_X    ...      STATE SHAPE_AREA
0                         Albany  117.899601    ...         WA   0.003012
1                  Albany Region  118.207172    ...         WA   0.394533
2  Alexander Heights - Koondoola  115.865812    ...         WA   0.000638
3             Alkimos - Eglinton  115.677976    ...         WA   0.003104
4           Applecross - Ardross  115.836085    ...         WA   0.000518
 
[5 rows x 5 columns]
>>> df1.to_csv(r"D:\Twitter Data\Data\test\Suburbs_AUS.csv", index=False)
