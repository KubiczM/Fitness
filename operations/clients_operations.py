from operations.file_operations import save_client_data


def create_client_data():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    gender = input("Gender [female/male]: ")
    body_weight = input("Body weight [kg]: ")
    height = input("Height [cm]: ")
    age = input("Age [years]: ")

    print("\nSpecify your activity:")
    print("1 -> Low")
    print("2 -> Moderate")
    print("3 -> Active lifestyle")
    print("4 -> Very active")
    activity = input("Enter a number [from the scale above]: ")

    print("\nSpecify your calories balance:")
    print("1 -> Deficit")
    print("2 -> N/A")
    print("3 -> Surplus")
    calories_balance = input("Enter a number [from the scale above]: ")

    leg_length = input("Leg length [cm / measure from foot to hips]: ")
    tibia_length = input("Tibia length [cm / measure from knee to ankle]: ")
    femur_length = input("Femur length [cm / measure from knee to hips]: ")
    wingspan = input("Wingspan [cm / measure from fingertip to fingertip]: ")
    ulna = input("Ulna [cm / measure from elbow to wrist]: ")
    humerus = input("Humerus [cm / measure from top of shoulder to elbow]: ")

    # Save data
    client_data = {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "body_weight": body_weight,
        "height": height,
        "age": age,
        "activity": activity,
        "calories_balance": calories_balance,
        "leg_length": leg_length,
        "tibia_length": tibia_length,
        "femur_length": femur_length,
        "wingspan": wingspan,
        "ulna": ulna,
        "humerus": humerus,
    }

    save_client_data(client_data)
