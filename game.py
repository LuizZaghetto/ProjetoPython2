import json 

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data_dict = {item["name"]: item for item in data}
    return data_dict

def show_description(data, location):
    print(data[location]["description"])

def gameplay(data, first_loc):
    location = first_loc
    while(True):
        print("1 - Show actual location description")
        print("q - Quit the game")
        user_input = input("Choose your option: ")
        if user_input == "1": show_description(data, location)
        elif user_input == "q": return 

data = load_json("game.json")

gameplay(data, "Dirtmouth")