import sys
import pandas as pd
 
SOFTWARE = {"Utilities", "Animation & Modeling", "Video Production",
            "Design & Illustration", "Web Publishing", "Software Training",
            "Audio Production", "Photo Editing", "Education", "Accounting"}
COLUMNS = ["appid", "name", "release_date", "developer", "publisher", "platforms",
           "genres", "price", "positive_ratings", "negative_ratings"]
 
source, destination, n = sys.argv[1], sys.argv[2], int(sys.argv[3])
df = pd.read_csv(source)
is_software = df["genres"].fillna("").str.split(";").map(lambda g: any(x in SOFTWARE for x in g))
games = df[~is_software].copy()
games["total"] = games["positive_ratings"] + games["negative_ratings"]
top = games.sort_values(["total", "appid"], ascending=[False, True]).head(n)
top[COLUMNS].to_csv(destination, index=False)

print(f"{len(df)} rows, {is_software.sum()} software removed, {len(top)} kept. Fewest ratings in subset: {top['total'].min()}")