from typing import List, Dict, Union


class Back:
    def __init__(self, wingspan: Union[float, int], height: Union[float, int]) -> None:
        self.wingspan: float = float(wingspan)
        self.height: float = float(height)

    def _get_exercises_and_conclusion(self, arm_type: str) -> Dict[str, List[str]]:
        exercises_map = {
            "long arms": {
                "exercises": [
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
                ],
                "conclusion": [
                    "Conclusion [back / long arms] -> order for easiest muscles to develop:",
                    "1. Easiest: Latissimus Dorsi",
                    "2. Middle: Rear Delts and Rhomboids",
                    "3. Hardest: Traps",
                ],
            },
            "short arms": {
                "exercises": [
                    "[Vertical] Shoulder Width Pull-Ups / Pulldown",
                    "[Vertical] Motorcycle Row",
                    "[Vertical] Wide Grip Pronated Lat Pulldown",
                    "[Horizontal] Pendlay Row",
                    "[Horizontal] Chest-Supported Row",
                    "[Lats] Straight-Arms Pulldown",
                    "[Lats] Dumbbell/Bar Pullover",
                    "[Lats] Pullover Machine",
                    "[Lats] Kayak Row",
                ],
                "conclusion": [
                    "Conclusion [back / short arms] -> order for easiest muscles to develop:",
                    "1. Easiest: Latissimus Dorsi",
                    "2. Middle: Rhomboids and Rear Delts",
                    "3. Hardest: Traps",
                ],
            },
        }

        return exercises_map.get(arm_type, {})

    def back_strategies(self) -> Dict[str, List[str]]:
        arm_type = "long arms" if self.wingspan > self.height else "short arms"
        strategies = self._get_exercises_and_conclusion(arm_type)

        return {
            arm_type: strategies.get("exercises", []),
            "conclusion": strategies.get("conclusion", []),
        }
