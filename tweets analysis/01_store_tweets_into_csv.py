import json
import os
import codecs

folderpath = r"D:\Twitter Data\Data"
files = os.listdir(folderpath)
os.chdir(folderpath)

fo = open(r"D:\Twitter Data\Data\test\tweets.csv", "w")
fo.write("\ufeff")
fo.write("id,created_at,coordinates,co_lon,co_lat,geo,geo_lat,geo_lon," + 
         "user_location,place_type,place_name," + 
         "place_full_name,place_country,place_bounding_box,pb_avg_lon,pb_avg_lat," + 
         "lang,source,text")
count = 0

for file in files:
    # determine is file or directory
    if os.path.isdir(file):
        continue
        
    count += 1
    print(count, ":", file)
    #if count < 100:
    #    continue
    
    tweets_file = open(file, "r")
    for line in tweets_file:
        try:
            #count += 1
            #if (count < 53850):
            #    continue
            tweet = json.loads(line)
            csv_text = "\n"
            # id
            csv_text += tweet["id_str"]
            csv_text += ","
            # created_at
            csv_text += str(tweet["created_at"])
            csv_text += ","
            # coordinates
            if (tweet["coordinates"]):
                csv_text += "Yes,"
                csv_text += str(tweet["coordinates"]["coordinates"][0])
                csv_text += ","
                csv_text += str(tweet["coordinates"]["coordinates"][1])
            else:
                csv_text += "None,None,None"
            csv_text += ","
            # geo
            if (tweet["geo"]):
                csv_text += "Yes,"
                csv_text += str(tweet["geo"]["coordinates"][0])
                csv_text += ","
                csv_text += str(tweet["geo"]["coordinates"][1])
            else:
                csv_text += "None,None,None"
            csv_text += ","
            # user->location
            ul = str(tweet["user"]["location"])
            ul = ul.replace("\n", " ")
            ul = ul.replace("\"", "")
            ul = ul.replace("\'", "")
            csv_text += "\"" + ul + "\""
            csv_text += ","
            # place->type
            csv_text += str(tweet["place"]["place_type"])
            csv_text += ","
            # place->name
            csv_text += "\"" + str(tweet["place"]["name"]) + "\""
            csv_text += ","
            # place->full_name
            csv_text += "\"" + str(tweet["place"]["full_name"]) + "\""
            csv_text += ","
            # place->country
            csv_text += "\"" + str(tweet["place"]["country"]) + "\""
            csv_text += ","
            # place->bounding_box
            if (tweet["place"]["bounding_box"]["coordinates"]):
                # min_lon
                min_lon = tweet["place"]["bounding_box"]["coordinates"][0][0][0]
                # min_lat
                min_lat = tweet["place"]["bounding_box"]["coordinates"][0][0][1]
                # max_lon
                max_lon = tweet["place"]["bounding_box"]["coordinates"][0][2][0]
                # max_lat
                max_lat = tweet["place"]["bounding_box"]["coordinates"][0][2][1]
                # avg of lon and lat
                lon = (min_lon + max_lon)/2
                lat = (min_lat + max_lat)/2
                csv_text += "Yes,"
                csv_text += str(lon)
                csv_text += ","
                csv_text += str(lat)
            else:
                csv_text += "None, None, None"
            csv_text += ","
            # lang
            csv_text += str(tweet["lang"])
            csv_text += ","
            # source
            csv_text += "\"" + str(tweet["source"]) + "\""
            csv_text += ","
            # text
            # replace carriage return, double quotation marks, single quotation marks with space or nothing
            text = str(tweet["text"])
            text = text.replace("\r", " ")
            text = text.replace("\n", " ")
            text = text.replace("\"", "")
            text = text.replace("\'", "")
            csv_text += "\"" + text + "\""
            fo.write(csv_text)
            #if (count > 53851):
            #    break
        except:
            continue
    
    #if count > 150:
    #    break
        
fo.close()   

import pandas as pd
df = pd.read_csv(open(r"D:\Twitter Data\Data\test\tweets.csv", encoding='utf-8',errors='ignore'))
df.head()
