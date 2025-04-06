import pytest
from unittest.mock import patch
from personal_info.upper_limbs import UpperLimbsMeasurements


@pytest.fixture
def measurements():
    return UpperLimbsMeasurements()


def test_wingspan_info_valid(measurements):
    with patch("builtins.input", side_effect=["180"]):
        assert measurements.wingspan_info() == 180.0


def test_wingspan_info_invalid_then_valid(measurements):
    with patch("builtins.input", side_effect=["abc", "-50", "175"]):
        assert measurements.wingspan_info() == 175.0


def test_ulna_info_valid(measurements):
    with patch("builtins.input", side_effect=["30"]):
        assert measurements.ulna_info() == 30.0


def test_ulna_info_invalid_then_valid(measurements):
    with patch("builtins.input", side_effect=["xyz", "-10", "25"]):
        assert measurements.ulna_info() == 25.0


def test_humerus_info_valid(measurements):
    with patch("builtins.input", side_effect=["40"]):
        assert measurements.humerus_info() == 40.0


def test_humerus_info_invalid_then_valid(measurements):
    with patch("builtins.input", side_effect=["!", "0", "45"]):
        assert measurements.humerus_info() == 45.0
