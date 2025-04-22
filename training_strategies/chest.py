from typing import List, Dict, Union


class Chest:
    def __init__(self, wingspan: Union[float, int], height: Union[float, int]) -> None:
        self.wingspan: float = float(wingspan)
        self.height: float = float(height)

    def _get_exercises_and_conclusion(self, arm_type: str) -> Dict[str, List[str]]:
        exercises_map = {
            "long arms": {
                "exercises": [
                    "Bench Press",
                    "Dips",
                    "Incline Dumbbells Press",
                    "Cable Flies",
                    "Peck Deck",
                    "Incline Dumbbells Flies",
                ]
            },
            "short arms": {
                "exercises": [
                    "Wide Grip Bench Press",
                    "Power Flies",
                    "Dumbbells Fly-Press",
                    "Peck Deck",
                    "Cable Flies",
                    "Squeeze Press",
                ]
            },
            "average arms": {
                "exercises": [
                    "Incline Bench Press",
                    "Flat Bench Press",
                    "Chest Dips",
                    "Dumbbell Press",
                    "Cable Chest Press",
                    "Machine Chest Press",
                ]
            },
        }

        conclusion = [
            "Conclusion -> order for easiest muscles to develop:",
            "1. Easiest: Pectorals",
            "2. Middle: Deltoids",
            "3. Hardest: Triceps",
        ]

        result = exercises_map.get(arm_type, {"exercises": []})
        result["conclusion"] = conclusion

        strategies = {
            "long arms": exercises_map.get("long arms", {}),
            "short arms": exercises_map.get("short arms", {}),
            "average arms": exercises_map.get("average arms", {}),
            "conclusion": conclusion,
        }

        return strategies

    def chest_strategies(self) -> Dict[str, List[str]]:
        if self.wingspan > self.height:
            arm_type = "long arms"
        elif 0.95 * self.height <= self.wingspan <= 1.05 * self.height:
            arm_type = "average arms"
        else:
            arm_type = "short arms"

        return self._get_exercises_and_conclusion(arm_type)
