"""
JSON Operations for Client Data Management

This script provides functions for managing client data stored in JSON files.
It includes functionalities to collect and save client data in a client-specific JSON file,
as well as to retrieve and display the saved client data from a specified JSON file.

Functions:
- create_client_data: Collects client data and saves it as a JSON file in the client-specific directory.
- open_client_data: Allows retrieving and displaying client data from a specified JSON file.

Usage:
- Use create_client_data() to generate and save a new JSON file with client data.
- Use open_client_data() to load and display the data from an existing JSON file.
"""

import json
import os
from datetime import datetime
from personal_info.general import PersonalInfo


def create_client_data():
    client = PersonalInfo()
    data = client.update_info()

    first_name = client.first_name.lower()
    last_name = client.last_name.lower()

    current_date = datetime.now().strftime("%d-%m-%Y")

    file_name = f"{first_name}_{last_name}_{current_date}.json"

    clients_directory = "clients"
    client_specific_directory = os.path.join(
        clients_directory, f"{first_name}_{last_name}"
    )

    if not os.path.exists(clients_directory):
        os.makedirs(clients_directory)

    if not os.path.exists(client_specific_directory):
        os.makedirs(client_specific_directory)

    file_path = os.path.join(client_specific_directory, file_name)

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

    print("The data has been saved to a file:", file_path)


def open_client_data():
    while True:
        clients_directory = "clients"
        print("\nAvailable client directories:")
        if os.path.exists(clients_directory):
            for client_dir in os.listdir(clients_directory):
                client_dir_path = os.path.join(clients_directory, client_dir)

                if os.path.isdir(client_dir_path):
                    print(f"\nClient: {client_dir}")
                    json_files = [f for f in os.listdir(client_dir_path) if f.endswith(".json")]
                    if json_files:
                        for idx, file in enumerate(json_files, start=1):
                            print(f"  {idx}. {file}")
                    else:
                        print("No JSON files found.")
        else:
            print("No client directories found.")

        client_name = input("\nEnter the client name (or type 'exit' to quit): ")

        if client_name.lower() == 'exit':
            break

        client_directory = os.path.join(clients_directory, client_name)

        if os.path.isdir(client_directory):
            json_files = [f for f in os.listdir(client_directory) if f.endswith(".json")]
            if json_files:
                print(f"\nContents of {client_name}:")
                for idx, file in enumerate(json_files, start=1):
                    print(f"{idx}. {file}")

                file_choice = input("\nEnter the number of the file to open: ")
                try:
                    file_name = json_files[int(file_choice) - 1]
                    file_path = os.path.join(client_directory, file_name)

                    if os.path.exists(file_path):
                        with open(file_path, "r") as file:
                            data = json.load(file)
                            print("Data loaded successfully:", data)
                        break
                except (ValueError, IndexError):
                    print("Invalid choice. Please try again.")
            else:
                print("No JSON files found for this client.")
        else:
            print(f"The directory for client '{client_name}' does not exist. Please try again.")



