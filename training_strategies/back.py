class Back:
    def __init__(self, wingspan, height):
        self.wingspan = wingspan
        self.height = height

    def back_strategies(self):
        if self.wingspan > self.height:
            back_long_arms = [
                "[Vertical] Close-Grip Supinated Chin-Up / Lat Pulldown",
                "[Horizontal] Pronated Grip Bent Over Row",
                "[Horizontal] Neutral Grip Seated Row",
                "[Horizontal] Chest-Supported Dumbbells Row",
                "[Horizontal] T-Bar Row",
                "[Mid-back] Reverse Peck Deck",
                "[Mid-back] Face Pull",
                "[Mid-back] Chest Supported Rear Delts",
                "[Traps] Kirk Shrugs",
                "[Traps] Dumbbells Shrugs",
                "[Traps] Upright Row",
            ]

            conclusion = [
                "Conclusion [back / short arms] -> order for easiest muscles to develop:"
                "1. Easiest: Latissimus Dorsi",
                "2. Middle: Rear Delts and Rhomboids",
                "3. Hardest: Traps",
            ]

            return {"long arms": back_long_arms, "conclusion": conclusion}

        elif self.wingspan <= self.height:
            back_short_arms = [
                "[Vertical] Shoulder Width Pull-Ups / Pulldown",
                "[Vertical] Motorcycle Row",
                "[Vertical] Wide Grip Pronated Lat Pulldown",
                "[Horizontal] Pendlay Row",
                "[Horizontal] Chest-Supported Row",
                "[Lats] Straight-Arms Pulldown",
                "[Lats] Dumbbell/Bar Pullover",
                "[Lats] Pullover Machine",
                "[Lats] Kayak Row",
            ]

            conclusion = [
                "Conclusion [back / short arms]: -> order for easiest muscles to develop:"
                "1. Easiest: Pectorals",
                "2. Middle: Deltoids",
                "3. Hardest: Triceps",
            ]

            return {"short arms": back_short_arms, "conclusion": conclusion}
