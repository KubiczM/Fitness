from training_strategies.chest import Chest


def test_chest_long_arms():
    chest = Chest(wingspan=190, height=180)
    strategies = chest.chest_strategies()

    assert "Bench Press" in strategies["long arms"]["exercises"]
    assert "Incline Dumbbells Press" in strategies["long arms"]["exercises"]
    assert len(strategies["long arms"]["exercises"]) == 6

    assert (
        "Conclusion -> order for easiest muscles to develop:"
        in strategies["conclusion"]
    )
    assert "1. Easiest: Pectorals" in strategies["conclusion"]
    assert len(strategies["conclusion"]) == 4


def test_chest_short_arms():
    chest = Chest(wingspan=170, height=180)
    strategies = chest.chest_strategies()

    assert "Wide Grip Bench Press" in strategies["short arms"]["exercises"]
    assert "Power Flies" in strategies["short arms"]["exercises"]
    assert len(strategies["short arms"]["exercises"]) == 6

    assert (
        "Conclusion -> order for easiest muscles to develop:"
        in strategies["conclusion"]
    )
    assert "1. Easiest: Pectorals" in strategies["conclusion"]
    assert len(strategies["conclusion"]) == 4


def test_chest_equal_wingspan():
    chest = Chest(wingspan=180, height=180)
    strategies = chest.chest_strategies()

    assert "Wide Grip Bench Press" in strategies["short arms"]["exercises"]
    assert "Power Flies" in strategies["short arms"]["exercises"]
    assert len(strategies["short arms"]["exercises"]) == 6

    assert (
        "Conclusion -> order for easiest muscles to develop:"
        in strategies["conclusion"]
    )
    assert "1. Easiest: Pectorals" in strategies["conclusion"]
    assert len(strategies["conclusion"]) == 4
