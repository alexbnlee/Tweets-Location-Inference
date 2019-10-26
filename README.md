## Tweets-Location-Inference

### Shapefile Processing
- Dissolve the same attribute (SA2_NAME)
- Add centroid XY
- Add a field called State
- Merge 8 polygons to one AUS
- Export table to csv
- Get speicfic columns

### Tweets Analysis
- Store tweets into csv
  - Replace carriage return into space (location and text)
  - Replace double quotation marks into nothing
  - Replace single quotation marks into nothing
  - Get average lon and lat from bouding_box

- Data cleaning
  - Delete duplicated tweets
  - Change time format (String -> Datetime)
  - Change coordinates format (String -> Float)
  - Get specific source info
  - Get Tweets with coordinates
  - Get Tweets in AUS (attribute)
  - Delete Tweets outside AUS (coordinates)
  
