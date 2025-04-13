from typing import List, Dict, Union

"""
Arms Training Strategies

This class provides exercise recommendations based on the relationship between wingspan and height,
focusing on biceps and triceps development.

Class:
- Arms: Offers exercise strategies for biceps and triceps training.

Methods:
- arms_strategies: Determines recommended exercises based on wingspan and height.

Usage:
Create an instance of `Arms` with wingspan and height, then call `arms_strategies` to get a list of suggested exercises.
The exercises are categorized into biceps and triceps routines.
"""


class Arms:
    def __init__(self, wingspan: Union[float, int], height: Union[float, int]) -> None:
        self.wingspan: float = float(wingspan)
        self.height: float = float(height)

    def arms_strategies(self) -> Dict[str, List[str]]:
        biceps_exercises: List[str] = []
        triceps_exercises: List[str] = []

        if self.wingspan > self.height:
            biceps_exercises = [
                "Barbell Curls",
                "Incline Dumbbells Curls",
                "Single Arm Preacher Curl",
                "Cable Curl",
                "Dumbbells Hammer Curl",
                "Cable Reverse Curl",
                "Machine Curl",
            ]
            triceps_exercises = [
                "JM Press",
                "Nosebreaker",
                "Overhead Dumbbell Triceps Extension",
                "Triceps Extension",
                "Rope Pressdown",
                "Decline Dumbbells Triceps Extension",
            ]
        else:
            biceps_exercises = [
                "Supinated Pull-Ups",
                "Neutral-Grip Pull-Ups",
                "Barbell Curl",
                "Preacher Curl",
                "Rope Hammer Curl",
                "Cable Curl",
            ]
            triceps_exercises = [
                "Close-Grip Bench Press",
                "Dips",
                "Reverse-Grip Bench Press",
                "Nosebreaker",
                "Decline Dumbbells Triceps Extension",
                "Triceps Pressdown",
            ]

        return {
            "biceps": biceps_exercises,
            "triceps": triceps_exercises,
        }
