import json
import pandas as pd
data=""

with open("restart-first-repo/JSON-example/countries.json", "r") as read_file:
    data=json.load(read_file)
    print(data)
    #print("Amount oF students: " + str(len(data)))

    
df = pd.read_json("restart-first-repo/JSON-example/countries.json")
print(df[df["population"]>=38000000])
print(len(df[df["population"]>=38000000]))
print("Mean of latitude is: " + str(df["latitude"].mean()))


#print(df.groupby(df["Strength"]).mean())