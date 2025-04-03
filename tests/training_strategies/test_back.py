from training_strategies.back import Back

def test_back_long_arms():
    back = Back(wingspan=190, height=180)
    strategies = back.back_strategies()

    assert "[Vertical] Close-Grip Supinated Chin-Up / Lat Pulldown" in strategies["long arms"]
    assert "[Traps] Upright Row" in strategies["long arms"]
    assert len(strategies["long arms"]) == 11
    assert "Conclusion [back / short arms]" in strategies["conclusion"][0]

def test_back_short_arms():
    back = Back(wingspan=170, height=180)
    strategies = back.back_strategies()

    assert "[Vertical] Shoulder Width Pull-Ups / Pulldown" in strategies["short arms"]
    assert "[Lats] Kayak Row" in strategies["short arms"]
    assert len(strategies["short arms"]) == 9
    assert "Conclusion [back / short arms]" in strategies["conclusion"][0]

def test_back_equal_wingspan():
    back = Back(wingspan=180, height=180)
    strategies = back.back_strategies()

    assert "[Vertical] Shoulder Width Pull-Ups / Pulldown" in strategies["short arms"]
    assert "[Lats] Pullover Machine" in strategies["short arms"]
    assert len(strategies["short arms"]) == 9
    assert "Conclusion [back / short arms]" in strategies["conclusion"][0]
