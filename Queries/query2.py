import csv
import pickle

def load_companies():
  with open("production_companies_table.csv", "r") as f:
    reader = csv.DictReader(f)
    return list(reader)

def load_movies():
  with open("movies_table.csv", "r") as f:
    reader = csv.DictReader(f)
    return list(reader)
  
def start_process():
  companies = load_companies()
  movies = load_movies()

  output = {}

  for c in companies:
      output[c["production_companies"]] = {
          "count": 0,
          "revenue": 0
          }

  for c in companies:
    for m in movies:
      if m["id"] == c["id"]:
          output[c["production_companies"]]["count"] += 1
          output[c["production_companies"]]["revenue"] += int(m["revenue"])
         
         
  final_output = {
      "small": 0,
      "medium": 0,
      "big": 0
      }
  
  
  small_count = 0
  medium_count = 0
  big_count = 0
  for c in output:
      if int(output[c]["count"]) <= 10:
          small_count += 1
          final_output["small"] += int(output[c]["revenue"])

      if 11<= int(output[c]["count"]) <= 50:
          medium_count += 1
          final_output["medium"] += int(output[c]["revenue"])
        
      if 50< int(output[c]["count"]):
          big_count += 1
          final_output["big"] += int(output[c]["revenue"])
        
        
  final_output["small"] = final_output["small"] / small_count
  final_output["medium"] = final_output["medium"] / medium_count
  final_output["big"] = final_output["big"] / big_count
  
  
  with open ("query2.pkl", "wb") as f1:
      pickle.dump(final_output,f1)
      
     
      
  
        

if __name__ == "__main__":
  start_process()