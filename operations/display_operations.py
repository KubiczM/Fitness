def display_client_data(client_data):

    print(f"\nClient: {client_data['first_name']} {client_data['last_name']}")
    print(f"Body weight: {client_data['body_weight']} kg")
    print(f"Height: {client_data['height']} cm")
    print(f"Age: {client_data['age']} years")
    print(f"Calories balance: {client_data['calories_balance']} cal\n")

    print("Body Measurements:")
    print(f"  Leg length: {client_data['leg_length']} cm")
    print(f"  Tibia length: {client_data['tibia_length']} cm")
    print(f"  Femur length: {client_data['femur_length']} cm")
    print(f"  Wingspan: {client_data['wingspan']} cm")
    print(f"  Ulna: {client_data['ulna']} cm")
    print(f"  Humerus: {client_data['humerus']} cm\n")

    def print_strategy(title, strategy_dict):
        print(f"{title}")
        for key, value in strategy_dict.items():
            print(f"\n  {key.capitalize()}:")
            for line in value:
                print(f"    - {line}")
        print()

    print_strategy("Arms Strategy", client_data["arms strategy"])
    print_strategy("Chest Strategy", client_data["chest strategy"])
    print_strategy("Back Strategy", client_data["back strategy"])
    print_strategy("Legs Strategy", client_data["legs strategy"])