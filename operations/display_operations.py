def display_client_data(client_data):

    print(f"\nClient: {client_data['first name']} {client_data['last name']}")
    print(f"Body weight: {client_data['body weight [kg]']} kg")
    print(f"Height: {client_data['height [cm]']} cm")
    print(f"Age: {client_data['age [years]']} years")
    print(f"Calories balance: {client_data['calories balance [cal]']} cal\n")

    print("Body Measurements:")
    print(f"  Leg length: {client_data['legs']['legs [cm]']} cm")
    print(f"  Tibia length: {client_data['legs']['tibia [cm]']} cm")
    print(f"  Femur length: {client_data['legs']['femur [cm]']} cm")
    print(f"  Wingspan: {client_data['upper limbs']['wingspan [cm]']} cm")
    print(f"  Ulna: {client_data['upper limbs']['ulna [cm]']} cm")
    print(f"  Humerus: {client_data['upper limbs']['humerus [cm]']} cm\n")

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
