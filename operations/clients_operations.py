from personal_info.general import PersonalInfo
from operations.file_operations import save_client_data
from typing import Optional, Dict, Any


def create_client_data() -> None:
    person = PersonalInfo()
    info: Optional[Dict[str, Any]] = person.update_info()

    if info is None:
        print("Error: No client data returned from update_info.")
        return

    save_client_data(info)
