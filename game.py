import json 
import time

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data_dict = {item["name"]: item for item in data}
    return data_dict

def show_description(data, location):
    print("\n" + data[location]["description"] + "\n")

def travel(data, location):
    exits = data[location]["exits"]
    
    if not exits:
        print("\nNo available paths from here.\n")
        return location
        
    print("\nAvailable ways:")
    for index, exit_name in enumerate(exits, 1): 
        print(f"{index} - {exit_name}")
    print("0 - Cancel travel\n")
        
    while True:
        try:
            choice = int(input("Choose the new location: "))
            
            if choice == 0:
                return location
            elif 1 <= choice <= len(exits):
                return exits[choice - 1]
            else:
                print("Error: Choose a valid number from the list.")
                
        except ValueError:
            print("Error: Please enter only integer numbers.")

def gameplay(data, first_loc):
    location = first_loc
    show_description(data, location)
    while(True):
        print(f"Actual location: {location}\n")

        print("1 - Show actual location description")
        print("2 - Travel")
        print("q - Quit the game\n")

        user_input = input("Choose your option: ")
        if user_input == "1": show_description(data, location)

        elif user_input == "2": 
            location = travel(data, location)
            show_description(data, location)

        elif user_input == "q": return 
        else: 
            print("\nPlease input a valid option", flush=True)
            time.sleep(2)

data = load_json("game.json")

gameplay(data, "Dirtmouth")