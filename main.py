from json_operations import create_client_data, open_client_data
import os

"""
Client Data Management System

This script allows creating, viewing, and retrieving client data stored in JSON files.
Each client has a unique directory where their data is saved.

Functions:
- create_client_data: Collects client data and saves it as a JSON file in a client-specific directory.
- open_client_data: Allows retrieving and displaying client data from a specified JSON file.
- list_saved_clients: Displays all saved client files and directories in the "clients" folder.
- run: Provides a command-line interface for users to create, view, or retrieve client data.

Usage:
Run the script and follow the prompts to either create new client data, open an existing client's data, or list all saved client files.
"""


def list_saved_clients():
    """
    Lists all saved client files in the "clients" directory.
    Allows the user to select a file to open based on the list.
    """
    clients_directory = "clients"

    if os.path.exists(clients_directory):
        print("\nSaved Client Files:")
        for client_dir in os.listdir(clients_directory):
            client_dir_path = os.path.join(clients_directory, client_dir)

            if os.path.isdir(client_dir_path):
                print(f"\nClient: {client_dir}")
                for file in os.listdir(client_dir_path):
                    if file.endswith(".json"):
                        print(f"- {file}")
    else:
        print("No saved client files found.")


def run():
    while True:
        print()
        choice = input(
            "Choose an option:\n1. Create Client Data\n2. Open Client Data\n3. List Saved Clients\n"
            "4. Exit\nEnter your choice: "
        )

        if choice == "1":
            create_client_data()
        elif choice == "2":
            open_client_data()
        elif choice == "3":
            list_saved_clients()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")



if __name__ == "__main__":
    run()
