import os
import json
from operations.display_operations import display_client_data


def save_client_data(client_data):
    client_dir = f"clients/{client_data['first_name']}_{client_data['last_name']}"
    os.makedirs(client_dir, exist_ok=True)

    file_name = f"{client_data['first_name']}_{client_data['last_name']}_{get_current_date()}.json"
    file_path = os.path.join(client_dir, file_name)

    with open(file_path, "w") as f:
        json.dump(client_data, f)

    print(f"\nThe data has been saved to a file: {file_path}\n")


def list_client_files(client_dir, selected_client):
    client_dir_path = os.path.join("clients", client_dir)
    if os.path.exists(client_dir_path):
        print(f"\nFiles for {selected_client}:")
        client_files = os.listdir(client_dir_path)
        for index, client_file in enumerate(client_files, 1):
            print(f"{index}. {client_file}")

        file_choice = input("Choose a file by number: ")

        try:
            file_choice = int(file_choice)
            if 1 <= file_choice <= len(client_files):
                file_path = os.path.join(client_dir_path, client_files[file_choice - 1])
                with open(file_path, "r") as f:
                    client_data = json.load(f)
                    display_client_data(client_data)
            else:
                print("Invalid choice, please choose a valid number.")
        except ValueError:
            print("Invalid input. Please choose a valid number.")
    else:
        print("Client files not found.")


def list_saved_clients():
    clients_dir = "clients"
    if os.path.exists(clients_dir):
        print("Saved Client Files:")
        clients = os.listdir(clients_dir)
        for index, client_dir in enumerate(clients, 1):
            print(f"{index}. {client_dir}")

        client_choice = input("Choose a client by number: ")

        try:
            client_choice = int(client_choice)
            if 1 <= client_choice <= len(clients):
                selected_client = clients[client_choice - 1]
                list_client_files(selected_client, selected_client)
            else:
                print("Invalid choice, please choose a valid number.")
        except ValueError:
            print("Invalid input. Please choose a valid number.")
    else:
        print("No saved clients found.")


def get_current_date():
    from datetime import datetime

    return datetime.now().strftime("%d-%m-%Y")