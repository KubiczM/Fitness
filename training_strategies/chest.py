class Chest:
    def __init__(self, wingspan, height):
        self.wingspan = wingspan
        self.height = height

    def chest_strategies(self):
        if self.wingspan > self.height:
            chest_long_arms = [
                "Bench Press",
                "Dips",
                "Incline Dumbbells Press",
                "Cable Flies",
                "Peck Deck",
                "Incline Dumbbells Flies",
            ]

            conclusion = [
                "Conclusion [chest / long arms] -> order for easiest muscles to develop:",
                "1. Easiest: Pectorals",
                "2. Middle: Deltoids",
                "3. Hardest: Triceps",
            ]

            return {"long arms": chest_long_arms, "conclusion": conclusion}

        elif self.wingspan <= self.height:
            chest_short_arms = [
                "Wide GripBench Press",
                "Power Flies",
                "Dumbbells Fly-Press",
                "Peck Deck",
                "Cable Flies",
                "Squeeze Press",
            ]

            conclusion = [
                "Conclusion [chest / short arms] -> order for easiest muscles to develop:",
                "1. Easiest: Pectorals",
                "2. Middle: Deltoids",
                "3. Hardest: Triceps",
            ]

            return {"short arms": chest_short_arms, "conclusion": conclusion}
