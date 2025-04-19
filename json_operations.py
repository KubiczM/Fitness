import json
import os
from datetime import datetime
from personal_info.general import PersonalInfo

"""
JSON Operations for Client Data Management

This script provides functions to manage client data stored in JSON files.
It allows you to create new client data, save it in a client-specific JSON file, and retrieve and display saved
client data.

Functions:
- create_client_data: Collects client data and saves it as a JSON file in a unique directory for each client.
- open_client_data: Retrieves and displays client data from a selected JSON file within a chosen client's directory.
- display_client_data: Displays the details of the selected client's data, including personal information,
body measurements, and workout strategies.

Usage:
- Use create_client_data() to gather and save a new client’s data into a JSON file.
- Use open_client_data() to select an existing client, browse their files, and view the saved data.
"""


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
    print("\nSaved Clients:")
    clients_directory = "clients"

    clients = []
    for client_dir in os.listdir(clients_directory):
        client_dir_path = os.path.join(clients_directory, client_dir)
        if os.path.isdir(client_dir_path):
            clients.append(client_dir)

    if not clients:
        print("No clients found.")
        return

    for index, client in enumerate(clients, start=1):
        print(f"{index}. {client}")

    client_choice = input("Choose a client by number: ")
    try:
        client_index = int(client_choice) - 1
        selected_client = clients[client_index]
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        return

    client_dir_path = os.path.join(clients_directory, selected_client)
    client_files = []
    for file in os.listdir(client_dir_path):
        if file.endswith(".json"):
            client_files.append(file)

    if not client_files:
        print(f"No data files found for {selected_client}.")
        return

    print(f"\nAvailable files for {selected_client}:")
    for index, file in enumerate(client_files, start=1):
        print(f"{index}. {file}")

    file_choice = input("Choose a file by number: ")
    try:
        file_index = int(file_choice) - 1
        selected_file = client_files[file_index]
    except (ValueError, IndexError):
        print("Invalid choice. Exiting.")
        return

    file_path = os.path.join(client_dir_path, selected_file)

    with open(file_path, "r") as file:
        data = json.load(file)

    display_client_data(data)


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