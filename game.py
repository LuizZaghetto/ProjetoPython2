import json 

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data_dict = {item["name"]: item for item in data}
    return data_dict

def show_description(data, location):
    print(data[location]["description"])

data = load_json("game.json")

location = data["Forgotten Crossroads"]["name"]
print(location)
show_description(data, location)