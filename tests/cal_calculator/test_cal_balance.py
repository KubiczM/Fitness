from cal_calculator.total_metabolic import TotalMetabolic
from cal_calculator.basic_metabolic import BasicMetabolic
from cal_calculator.cal_balance import CalBalance

def test_cal_balance_deficit():
    basic_metabolic = BasicMetabolic(sex="male", body_weight=70, height=165, age=30)
    total_metabolic = TotalMetabolic(activity=2, basic_metabolic=basic_metabolic)
    total_metabolic_rate = total_metabolic.total_metabolic()

    cal_balance = CalBalance(total_metabolic=total_metabolic, question=1)

    result = cal_balance.balance_cal()

    assert result == round(total_metabolic_rate * 0.85)

def test_cal_balance_maintenance():
    basic_metabolic = BasicMetabolic(sex="male", body_weight=70, height=165, age=30)
    total_metabolic = TotalMetabolic(activity=2, basic_metabolic=basic_metabolic)
    total_metabolic_rate = total_metabolic.total_metabolic()

    cal_balance = CalBalance(total_metabolic=total_metabolic, question=2)

    result = cal_balance.balance_cal()

    assert result == round(total_metabolic_rate)

def test_cal_balance_over():
    basic_metabolic = BasicMetabolic(sex="male", body_weight=70, height=165, age=30)
    total_metabolic = TotalMetabolic(activity=2, basic_metabolic=basic_metabolic)
    total_metabolic_rate = total_metabolic.total_metabolic()

    cal_balance = CalBalance(total_metabolic=total_metabolic, question=3)

    result = cal_balance.balance_cal()

    assert result == round(total_metabolic_rate * 1.15)
