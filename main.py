import json
import os
from datetime import datetime
from personal_info.general import PersonalInfo


def create_json_file():
    client = PersonalInfo()
    data = client.update_info()

    first_name = client.first_name.lower()
    last_name = client.last_name.lower()

    current_date = datetime.now().strftime("%d-%m-%Y")

    file_name = f"{first_name}_{last_name}_{current_date}.json"

    clients_directory = "clients"
    client_specific_directory = os.path.join(clients_directory, f"{first_name}_{last_name}")

    if not os.path.exists(clients_directory):
        os.makedirs(clients_directory)

    if not os.path.exists(client_specific_directory):
        os.makedirs(client_specific_directory)

    file_path = os.path.join(client_specific_directory, file_name)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("The data has been saved to a file:", file_path)


def open_json_file():
    while True:
        file_name = input("Name of the file to open: ")

        clients_directory = "clients"
        file_path = os.path.join(clients_directory, file_name)

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = json.load(file)
                print("Data loaded successfully:", data)
        else:
            print("File", file_name, "does not exist in the directory", clients_directory)
        continue


create_json_file()
# open_json_file()
