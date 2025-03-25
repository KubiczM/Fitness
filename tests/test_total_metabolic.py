import pytest
from cal_calculator.total_metabolic import TotalMetabolic
from cal_calculator.basic_metabolic import BasicMetabolic


@pytest.fixture
def basic_metabolic():
    return BasicMetabolic(sex="female", body_weight=70, height=165, age=30)


def test_total_metabolic_sedentary(basic_metabolic):
    bmr = basic_metabolic.basic_metabolic()
    total_metabolic = TotalMetabolic(activity=1, basic_metabolic=basic_metabolic)
    assert total_metabolic.total_metabolic() == round(bmr * 1.4)


def test_total_metabolic_moderate(basic_metabolic):
    bmr = basic_metabolic.basic_metabolic()
    total_metabolic = TotalMetabolic(activity=2, basic_metabolic=basic_metabolic)
    assert total_metabolic.total_metabolic() == round(bmr * 1.6)


def test_total_metabolic_intense(basic_metabolic):
    bmr = basic_metabolic.basic_metabolic()
    total_metabolic = TotalMetabolic(activity=3, basic_metabolic=basic_metabolic)
    assert total_metabolic.total_metabolic() == round(bmr * 1.8)


def test_total_metabolic_very_intense(basic_metabolic):
    bmr = basic_metabolic.basic_metabolic()
    total_metabolic = TotalMetabolic(activity=4, basic_metabolic=basic_metabolic)
    assert total_metabolic.total_metabolic() == round(bmr * 2)
