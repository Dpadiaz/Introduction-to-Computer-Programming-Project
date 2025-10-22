import csv
import json
import pickle

ranges = []

for i in range(0, 100, 10):
    ranges.append((i, i+10))
    
country_budget = {}

with open("movies_table.csv", "r") as f:
    line = csv.DictReader(f)
    movies = {i["id"]: int(i["budget"]) for i in line}
    
with open("production_countries_table.csv", "r") as f:
    line = csv.DictReader(f)
    for i in line:
        ID =  i["id"]
        if ID not in movies:
            continue
        
        
        countries = json.loads(i["production_countries"])
        budget = movies[ID]
        
        range1 = None
        for start, end in ranges:
            if start*1000000 <= budget < end*1000000:
                range1 = f"{start}-{end}M"
                break
        
        if range1:
            for country in countries:
                name = country["name"]
                if name not in country_budget:
                    range_count = {}
                    for start, end in ranges:
                        range_count[f"{start}-{end}M"] = 0
                    country_budget[name] = range_count
                country_budget[name][range1] += 1              

with open("query1.pkl", "wb") as output:
    pickle.dump(country_budget, output)