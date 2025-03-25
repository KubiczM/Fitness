from cal_calculator.basic_metabolic import BasicMetabolic


def test_bmr_female():
    bmr = BasicMetabolic(sex="female", body_weight=70, height=165, age=30)
    assert bmr.basic_metabolic() == 1489


def test_bmr_male():
    bmr = BasicMetabolic(sex="male", body_weight=80, height=175, age=25)
    assert bmr.basic_metabolic() == 1873
