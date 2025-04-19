from typing import List, Dict, Union


"""
Legs Training Strategies

This class provides exercise recommendations based on the relationship between leg length and height,
focused on leg development, including quads, hamstrings, glutes, and calves.

Class:
- Legs: Offers exercise strategies for leg training.

Methods:
- legs_strategies: Determines recommended exercises based on leg length and height.

Usage:
Create an instance of `Legs` with leg length, tibia, height, and femur measurements,
then call `legs_strategies` to get a list of suggested exercises.
The exercises are categorized based on whether the individual has long or short legs.
A conclusion is provided for which muscles are easiest to develop based on leg length.
"""


class Legs:
    def __init__(
        self,
        legs: Union[float, int],
        tibia: Union[float, int],
        height: Union[float, int],
        femur: Union[float, int],
    ) -> None:
        self.legs: float = float(legs)
        self.tibia: float = float(tibia)
        self.height: float = float(height)
        self.femur: float = float(femur)

    def legs_strategies(self) -> Dict[str, List[str]]:
        if self.legs >= 0.43 * self.height:
            long_legs: List[str] = [
                "[Squat pattern] Front Squat",
                "[Squat pattern] Heels Elevated Front Squat",
                "[Squat pattern] High Bar Heels Elevated Back Squat",
                "[Squat pattern] High Bar Heels Elevated Parallel Back Squat (Narrow Stance)",
                "[Hinge pattern] Deadlift [any variations]",
                "[Hip thrust] Will be effective, but not required unless want to max out the glutes",
                "[Single leg] Shorter Steps Walking Lunges",
                "[Single leg] Short Steps Bulgarian Split Squat",
                "[Single leg] Backwards Walking Lunges",
                "[Single leg] Backward Sled Pull",
                "[Assistance excercise] Hack Squat",
                "[Assistance excercise] Narrow Stance Leg Press",
                "[Assistance excercise] Leg Extension",
            ]

            conclusion: List[str] = [
                "Conclusion [long legs] -> order for easiest muscles to develop:",
                "1. Easiest: Quads",
                "2. Middle: Calves",
                "3. Hardest: Hamstrings and Glutes",
            ]

            return {"long legs": long_legs, "conclusion": conclusion}

        elif 0.44 * self.height <= self.legs <= 0.47 * self.height:
            if self.tibia >= 0.84 * self.femur:
                average_legs_short_tibia: List[str] = [
                    "[Squat pattern] Front Squat",
                    "[Squat pattern] Heels Elevated Front Squat",
                    "[Squat pattern] High Bar Heels Elevated Back Squat",
                    "[Squat pattern] High Bar Heels Elevated Parallel Back Squat (Narrow Stance)",
                    "[Hinge pattern] Deadlift [any variations]",
                    "[Hip thrust] Will be effective, but not required unless want to max out the glutes",
                    "[Single leg] Shorter Steps Walking Lunges",
                    "[Single leg] Short Steps Bulgarian Split Squat",
                    "[Single leg] Backwards Walking Lunges",
                    "[Single leg] Backward Sled Pull",
                    "[Assistance excercise] Hack Squat",
                    "[Assistance excercise] Narrow Stance Leg Press",
                    "[Assistance excercise] Leg Extension",
                ]

                conclusion: List[str] = [
                    "Conclusion [short legs] -> order for easiest muscles to develop:",
                    "1. Easiest: Glutes",
                    "2. Middle: Hamstrings",
                    "3. Hardest: Quads and Calves",
                ]

                return {
                    "average legs - short tibia": average_legs_short_tibia,
                    "conclusion": conclusion,
                }

            elif self.tibia <= 0.85 * self.femur:
                average_legs_long_tibia: List[str] = [
                    "[Squat pattern] Squat [and variations]",
                    "[Hinge pattern] Front Feet Elevated Romanian Deadlift",
                    "[Hip thrust] Back Extension",
                    "[Hip thrust] Reverse Hypers",
                    "[Single leg] Longer Steps Split Squat",
                    "[Single leg] Single-Leg Romanian Deadlift",
                    "[Single leg] Long Step Split Squat Front Foot Elevated",
                    "[Single leg] Low Handles Prowler Pushing",
                    "[Assistance excercise] Leg Curls",
                    "[Assistance excercise] Wider Feet Leg Press",
                    "[Assistance excercise] Glute-Ham Raise",
                    "[Assistance excercise] Rope Pull-Through",
                ]

                conclusion: List[str] = [
                    "Conclusion [long legs] -> order for easiest muscles to develop:",
                    "1. Easiest: Quads",
                    "2. Middle: Calves",
                    "3. Hardest: Hamstrings and Glutes",
                ]

                return {
                    "average legs - long tibia": average_legs_long_tibia,
                    "conclusion": conclusion,
                }

        elif self.legs < 0.43 * self.height:
            short_legs: List[str] = [
                "[Squat pattern] Squat [and variations]",
                "[Hinge pattern] Front Feet Elevated Romanian Deadlift",
                "[Hip thrust] Back Extension",
                "[Hip thrust] Reverse Hypers",
                "[Single leg] Longer Steps Split Squat",
                "[Single leg] Single-Leg Romanian Deadlift",
                "[Single leg] Long Step Split Squat Front Foot Elevated",
                "[Single leg] Low Handles Prowler Pushing",
                "[Assistance excercise] Leg Curls",
                "[Assistance excercise] Wider Feet Leg Press",
                "[Assistance excercise] Glute-Ham Raise",
                "[Assistance excercise] Rope Pull-Through",
            ]

            conclusion: List[str] = [
                "Conclusion [short legs] -> order for easiest muscles to develop:",
                "1. Easiest: Glutes",
                "2. Middle: Hamstrings",
                "3. Hardest: Quads and Calves",
            ]

            return {"short legs": short_legs, "conclusion": conclusion}

        else:
            return {
                "message": ["No leg strategy matched the provided proportions."],
                "conclusion": ["Please check the measurements."],
            }
