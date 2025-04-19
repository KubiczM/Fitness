from typing import List, Dict, Union


"""
Chest Training Strategies

This class provides exercise recommendations based on the relationship between wingspan and height,
focused on chest development, including pectorals, deltoids, and triceps.

Class:
- Chest: Offers exercise strategies for chest training.

Methods:
- chest_strategies: Determines recommended exercises based on wingspan and height.

Usage:
Create an instance of `Chest` with wingspan and height, then call `chest_strategies` to get a list of 
suggested exercises. The exercises are categorized based on whether the individual has long or short arms.
A conclusion is provided for which muscles are easiest to develop based on arm length.
"""


class Chest:
    def __init__(self, wingspan: Union[float, int], height: Union[float, int]) -> None:
        self.wingspan: float = float(wingspan)
        self.height: float = float(height)

    def _get_exercises_and_conclusion(self, arm_type: str) -> Dict[str, Union[List[str], List[str]]]:
        exercises_map = {
            "long arms": [
                "Bench Press",
                "Dips",
                "Incline Dumbbells Press",
                "Cable Flies",
                "Peck Deck",
                "Incline Dumbbells Flies",
            ],
            "short arms": [
                "Wide Grip Bench Press",
                "Power Flies",
                "Dumbbells Fly-Press",
                "Peck Deck",
                "Cable Flies",
                "Squeeze Press",
            ],
            "average arms": [
                "Incline Bench Press",
                "Flat Bench Press",
                "Chest Dips",
                "Dumbbell Press",
                "Cable Chest Press",
                "Machine Chest Press",
            ]
        }

        conclusion = [
            "Conclusion -> order for easiest muscles to develop:",
            "1. Easiest: Pectorals",
            "2. Middle: Deltoids",
            "3. Hardest: Triceps",
        ]

        exercises = exercises_map.get(arm_type, [])
        return {"exercises": exercises, "conclusion": conclusion}

    def chest_strategies(self) -> Dict[str, Union[List[str], List[str]]]:
        if self.wingspan > self.height:
            return self._get_exercises_and_conclusion("long arms")
        elif 0.95 * self.height <= self.wingspan <= 1.05 * self.height:
            return self._get_exercises_and_conclusion("average arms")
        else:
            return self._get_exercises_and_conclusion("short arms")
