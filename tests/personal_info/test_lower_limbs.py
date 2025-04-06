import pytest
from unittest.mock import patch
from personal_info.lower_limbs import LowerLimbsMeasurements


@pytest.fixture
def measurements():
    return LowerLimbsMeasurements()


def test_legs_info_valid(measurements):
    with patch("builtins.input", side_effect=["90"]):
        assert measurements.legs_info() == 90.0


def test_legs_info_invalid_then_valid(measurements):
    with patch("builtins.input", side_effect=["abc", "-10", "85"]):
        assert measurements.legs_info() == 85.0


def test_tibia_info_valid(measurements):
    with patch("builtins.input", side_effect=["40"]):
        assert measurements.tibia_info() == 40.0


def test_tibia_info_invalid_then_valid(measurements):
    with patch("builtins.input", side_effect=["xyz", "-5", "50"]):
        assert measurements.tibia_info() == 50.0


def test_femur_info_valid(measurements):
    with patch("builtins.input", side_effect=["50"]):
        assert measurements.femur_info() == 50.0


def test_femur_info_invalid_then_valid(measurements):
    with patch("builtins.input", side_effect=["!", "0", "55"]):
        assert measurements.femur_info() == 55.0
