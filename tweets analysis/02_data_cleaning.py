import pandas as pd

# read csv file
df = pd.read_csv(open(r"D:\Twitter Data\Data\test\tweets.csv", encoding='utf-8',errors='ignore'))

# drop duplicated tweets based on id
df = df.drop_duplicates(["id"])

# convert string to datetime format
# can get specific year, month, day, hour, minute and second info directly
df = df.astype({"created_at":"datetime64[ns]"})

# save as a new csv file with above changes
df.to_csv(r"D:\Twitter Data\Data\test\tweets_drop_duplicates1.csv", index = False)

# read the new csv file and see what will happen, lol
df = pd.read_csv(r"D:\Twitter Data\Data\test\tweets_drop_duplicates1.csv")
df.head()
