from personal_info.general import PersonalInfo
from operations.file_operations import save_client_data


def create_client_data():
    person = PersonalInfo()
    info = person.update_info()

    if info is None:
        print("Error: No client data returned from update_info.")
        return

    save_client_data(info)
