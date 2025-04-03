from training_strategies.arms import Arms


def test_arms_long_wingspan():
    arms = Arms(wingspan=190, height=180)
    strategies = arms.arms_strategies()

    assert "Barbell Curls" in strategies["biceps"]
    assert "JM Press" in strategies["triceps"]
    assert len(strategies["biceps"]) == 7
    assert len(strategies["triceps"]) == 6


def test_arms_short_wingspan():
    arms = Arms(wingspan=170, height=180)
    strategies = arms.arms_strategies()

    assert "Supinated Pull_Ups" in strategies["biceps"]
    assert "Close-Grip Bench Press" in strategies["triceps"]
    assert len(strategies["biceps"]) == 6
    assert len(strategies["triceps"]) == 6


def test_arms_equal_wingspan():
    arms = Arms(wingspan=180, height=180)
    strategies = arms.arms_strategies()

    assert "Supinated Pull_Ups" in strategies["biceps"]
    assert "Close-Grip Bench Press" in strategies["triceps"]
    assert len(strategies["biceps"]) == 6
    assert len(strategies["triceps"]) == 6
