from operations.clients_operations import create_client_data
from operations.file_operations import list_saved_clients


def run() -> None:
    while True:
        print()
        choice = input(
            "Choose an option:\n1. Create Client Data\n2. List Saved Clients\n3. Exit\nEnter your choice: "
        )
        print()

        if choice == "1":
            create_client_data()
        elif choice == "2":
            list_saved_clients()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    run()
