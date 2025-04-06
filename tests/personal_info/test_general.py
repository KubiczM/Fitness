import pytest
from unittest.mock import patch
from personal_info.general import PersonalInfo


@pytest.fixture
def personal_info():
    return PersonalInfo()


def test_first_name_info_valid(personal_info):
    with patch("builtins.input", return_value="Michael"):
        assert personal_info.first_name_info() == "Michael"


def test_first_name_info_invalid_then_valid(personal_info):
    with patch("builtins.input", side_effect=["123", "Michael"]):
        assert personal_info.first_name_info() == "Michael"


def test_last_name_info_valid(personal_info):
    with patch("builtins.input", return_value="Kubicz"):
        assert personal_info.last_name_info() == "Kubicz"


def test_last_name_info_invalid_then_valid(personal_info):
    with patch("builtins.input", side_effect=["Kubicz123", "Kubicz"]):
        assert personal_info.last_name_info() == "Kubicz"


def test_sex_info_valid(personal_info):
    with patch("builtins.input", return_value="male"):
        assert personal_info.sex_info() == "male"


def test_sex_info_invalid_then_valid(personal_info):
    with patch("builtins.input", side_effect=["other", "male"]):
        assert personal_info.sex_info() == "male"


def test_body_weight_info_valid(personal_info):
    with patch("builtins.input", return_value="75"):
        assert personal_info.body_weight_info() == 75.0


def test_body_weight_info_invalid_then_valid(personal_info):
    with patch("builtins.input", side_effect=["abc", "-10", "70"]):
        assert personal_info.body_weight_info() == 70.0


def test_height_info_valid(personal_info):
    with patch("builtins.input", return_value="180"):
        assert personal_info.height_info() == 180.0


def test_height_info_invalid_then_valid(personal_info):
    with patch("builtins.input", side_effect=["xyz", "-5", "175"]):
        assert personal_info.height_info() == 175.0


def test_age_info_valid(personal_info):
    with patch("builtins.input", return_value="25"):
        assert personal_info.age_info() == 25.0


def test_age_info_invalid_then_valid(personal_info):
    with patch("builtins.input", side_effect=["!", "0", "30"]):
        assert personal_info.age_info() == 30.0


def test_activity_info_valid(personal_info):
    with patch("builtins.input", return_value="3"):
        assert personal_info.activity_info() == 3


def test_activity_info_invalid_then_valid(personal_info):
    with patch("builtins.input", side_effect=["abc", "0", "2"]):
        assert personal_info.activity_info() == 2


def test_balance_cal_info_valid(personal_info):
    with patch("builtins.input", return_value="1"):
        assert personal_info.balance_cal_info() == 1


def test_balance_cal_info_invalid_then_valid(personal_info):
    with patch("builtins.input", side_effect=["abc", "0", "3"]):
        assert personal_info.balance_cal_info() == 3
