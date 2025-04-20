from typing import List, Dict, Union


class Arms:
    def __init__(self, wingspan: Union[float, int], height: Union[float, int]) -> None:
        self.wingspan: float = float(wingspan)
        self.height: float = float(height)

    def _get_exercises_and_conclusion(self, arm_type: str) -> Dict[str, List[str]]:
        exercises_map = {
            "long arms": {
                "biceps": [
                    "Barbell Curls",
                    "Incline Dumbbells Curls",
                    "Single Arm Preacher Curl",
                    "Cable Curl",
                    "Dumbbells Hammer Curl",
                    "Cable Reverse Curl",
                    "Machine Curl",
                ],
                "triceps": [
                    "JM Press",
                    "Nosebreaker",
                    "Overhead Dumbbell Triceps Extension",
                    "Triceps Extension",
                    "Rope Pressdown",
                    "Decline Dumbbells Triceps Extension",
                ],
                "conclusion": [
                    "Conclusion [arms / long arms] -> order for easiest muscles to develop:",
                    "1. Easiest: Biceps",
                    "2. Middle: Triceps",
                ],
            },
            "short arms": {
                "biceps": [
                    "Supinated Pull-Ups",
                    "Neutral-Grip Pull-Ups",
                    "Barbell Curl",
                    "Preacher Curl",
                    "Rope Hammer Curl",
                    "Cable Curl",
                ],
                "triceps": [
                    "Close-Grip Bench Press",
                    "Dips",
                    "Reverse-Grip Bench Press",
                    "Nosebreaker",
                    "Decline Dumbbells Triceps Extension",
                    "Triceps Pressdown",
                ],
                "conclusion": [
                    "Conclusion [arms / short arms] -> order for easiest muscles to develop:",
                    "1. Easiest: Biceps",
                    "2. Middle: Triceps",
                ],
            },
        }

        return exercises_map.get(arm_type, {})

    def arms_strategies(self) -> Dict[str, List[str]]:
        if self.wingspan > self.height:
            arm_type = "long arms"
        else:
            arm_type = "short arms"

        return self._get_exercises_and_conclusion(arm_type)
