import csv
import pickle


def load_companies():
    with open("csv/production_companies_table.csv", "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def load_genres():
    with open("csv/genres_table.csv", "r") as f:
        reader = csv.DictReader(f)
        return list(reader)


def start_process():
    companies = load_companies()
    genres = load_genres()

    output = {}

    for movie in companies:
        # movie = {"id": "91314", "production_companies": "Revolution Sun Studios"}
        for g in genres:
            # g = {'id': '2900', 'genres': 'Drama'}
            if g["id"] == movie["id"]:
                output[movie["production_companies"]] = output.get(
                    movie["production_companies"], {}
                )
                output[movie["production_companies"]][g["genres"]] = (
                    output[movie["production_companies"]].get(g["genres"], 0) + 1
                )

    with open("query3.pkl", "wb") as f:
        pickle.dump(output, f)
    print(output)


if __name__ == "__main__":
    start_process()
