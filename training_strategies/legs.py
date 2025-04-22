from typing import List, Dict, Union


class Legs:
    def __init__(
        self,
        leg_length: Union[float, int],
        tibia_length: Union[float, int],
        torso_length: Union[float, int],
    ) -> None:
        self.leg_length: float = float(leg_length)
        self.tibia_length: float = float(tibia_length)
        self.torso_length: float = float(torso_length)

    def _get_exercises_and_conclusion(self, leg_type: str) -> Dict[str, List[str]]:
        exercises_map = {
            "long legs": [
                "Low Bar Squat",
                "Front Foot Elevated Split Squat",
                "Romanian Deadlift",
                "Leg Curl",
                "Hip Thrust",
                "45 Degree Back Extension",
            ],
            "average legs - short tibia": [
                "High Bar Squat",
                "Cyclist Squat",
                "Heels Elevated Front Squat",
                "Split Squat",
                "Leg Press",
                "Hip Thrust",
                "Leg Curl",
            ],
            "average legs - long tibia": [
                "Trap Bar Deadlift",
                "Box Squat",
                "Leg Press",
                "Romanian Deadlift",
                "Hip Thrust",
                "Reverse Lunge",
            ],
            "short legs": [
                "High Bar Squat",
                "Front Squat",
                "Split Squat",
                "Leg Extension",
                "Lying Leg Curl",
                "Hip Thrust",
            ],
        }

        conclusion_map = {
            "long legs": [
                "Conclusion [legs / long legs]:",
                "Easiest to develop: Hamstrings & Glutes",
                "Middle: Quads",
                "Hardest: Overall Squatting Mechanics",
            ],
            "average legs - short tibia": [
                "Conclusion [legs / avg legs - short tibia]:",
                "Easiest to develop: Quads",
                "Middle: Glutes",
                "Hardest: Hamstrings",
            ],
            "average legs - long tibia": [
                "Conclusion [legs / avg legs - long tibia]:",
                "Easiest to develop: Glutes & Hamstrings",
                "Middle: Quads",
                "Hardest: Squat Depth/Balance",
            ],
            "short legs": [
                "Conclusion [legs / short legs]:",
                "Easiest to develop: Quads",
                "Middle: Glutes",
                "Hardest: Hamstrings",
            ],
        }

        return {
            leg_type: exercises_map.get(leg_type, []),
            "conclusion": conclusion_map.get(leg_type, []),
        }

    def leg_strategies(self) -> Dict[str, List[str]]:
        if self.leg_length > self.torso_length:
            leg_type = "long legs"
        elif self.leg_length < self.torso_length:
            if self.tibia_length < (self.leg_length * 0.45):
                leg_type = "average legs - short tibia"
            else:
                leg_type = "average legs - long tibia"
        else:
            leg_type = "short legs"

        return self._get_exercises_and_conclusion(leg_type)
