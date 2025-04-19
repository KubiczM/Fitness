import json
import os
from json_operations import create_client_data, open_client_data

"""
Client Data Management System

This script allows creating, viewing, and retrieving client data stored in JSON files.
Each client has a unique directory where their data is saved, and each directory may contain multiple JSON files.

Functions:
- create_client_data: Collects and saves client data as a JSON file in a client-specific directory.
- open_client_data: Retrieves and displays client data from a selected JSON file.
- list_saved_clients: Displays all client directories, allowing the user to choose a client to view or open their data.
- list_client_files: Lists JSON files in the selected client's directory for file selection.
- display_client_data: Displays detailed information about the selected client’s data.
- run: Provides the main command-line interface for interacting with the system.

Usage:
- Select an option to create, view, or manage client data.
"""


def list_saved_clients():
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


def list_client_files(client_dir):
    client_dir_path = os.path.join("clients", client_dir)
    files = [f for f in os.listdir(client_dir_path) if f.endswith(".json")]

    if not files:
        print(f"No JSON files found for {client_dir}.")
        return

    print(f"\nAvailable files for {client_dir}:")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")

    file_choice = input("Choose a file by number: ")

    try:
        file_choice = int(file_choice)
        if 1 <= file_choice <= len(files):
            selected_file = files[file_choice - 1]
            file_path = os.path.join(client_dir_path, selected_file)
            with open(file_path, "r") as file:
                data = json.load(file)
                display_client_data(data)
        else:
            print("Invalid choice, please choose a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def display_client_data(data):
    print("\nClient Data:")
    print(f"First Name: {data['first name']}")
    print(f"Last Name: {data['last name']}")
    print(f"Sex: {data['sex']}")
    print(f"Body Weight: {data['body weight [kg]']} kg")
    print(f"Height: {data['height [cm]']} cm")
    print(f"Age: {data['age [years]']} years")
    print(f"Basic Metabolic Rate: {data['basic metabolic [cal]']} cal")
    print(f"Total Metabolic Rate: {data['total metabolic [cal]']} cal")
    print(f"Calories Balance: {data['calories balance [cal]']} cal")

    print("\nLegs Measurements:")
    print(f"- Legs: {data['legs']['legs [cm]']} cm")
    print(f"- Tibia: {data['legs']['tibia [cm]']} cm")
    print(f"- Femur: {data['legs']['femur [cm]']} cm")

    print("\nUpper Limbs Measurements:")
    print(f"- Wingspan: {data['upper limbs']['wingspan [cm]']} cm")
    print(f"- Ulna: {data['upper limbs']['ulna [cm]']} cm")
    print(f"- Humerus: {data['upper limbs']['humerus [cm]']} cm")

    print("\nArms Strategy:")
    print("Biceps Exercises:")
    for exercise in data["arms strategy"]["biceps"]:
        print(f"  - {exercise}")

    print("Triceps Exercises:")
    for exercise in data["arms strategy"]["triceps"]:
        print(f"  - {exercise}")

    print("\nChest Strategy:")
    print("Exercises based on arms length:")

    arm_type = (
        "long arms" if data["upper limbs"]["wingspan [cm]"] > 150 else "short arms"
    )

    if arm_type in data["chest strategy"]:
        for exercise in data["chest strategy"][arm_type]:
            print(f"  - {exercise}")
    else:
        print(f"No exercises found for {arm_type}.")

    print("\nConclusion for Chest:")
    for line in data["chest strategy"]["conclusion"]:
        print(f"  - {line}")

    print("\nBack Strategy:")
    print("Exercises based on arms length:")

    if arm_type in data["back strategy"]:
        for exercise in data["back strategy"][arm_type]:
            print(f"  - {exercise}")
    else:
        print(f"No exercises found for {arm_type}.")

    print("\nConclusion for Back:")
    for line in data["back strategy"]["conclusion"]:
        print(f"  - {line}")

    print("\nLegs Strategy:")
    leg_type = "short legs" if data["legs"]["legs [cm]"] < 50 else "long legs"

    if leg_type in data["legs strategy"]:
        for exercise in data["legs strategy"][leg_type]:
            print(f"  - {exercise}")
    else:
        print(f"No exercises found for {leg_type}.")

    print("\nConclusion for Legs:")
    for line in data["legs strategy"]["conclusion"]:
        print(f"  - {line}")


def run():
    while True:
        print()
        choice = input(
            "Choose an option:\n1. Create Client Data\n2. List Saved Clients\n3. Open Client Data\n"
            "4. Exit\nEnter your choice: "
        )
        print()

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