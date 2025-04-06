"""
Upper Limb Measurements

This class collects and stores measurements of the upper limbs,
including wingspan, ulna, and humerus lengths.

Class:
- UpperLimbsMeasurements: Handles user input for upper limb dimensions.

Methods:
- wingspan_info: Captures wingspan length from fingertip to fingertip.
- ulna_info: Captures ulna length from elbow to wrist.
- humerus_info: Captures humerus length from shoulder to elbow.

Usage:
Create an instance of `UpperLimbsMeasurements` and call methods to input measurements.
Values are validated to ensure correctness.
"""


class UpperLimbsMeasurements:
    def __init__(self):
        self.wingspan = 0
        self.ulna = 0
        self.humerus = 0

    def wingspan_info(self):
        while True:

            try:
                self.wingspan = float(
                    input(
                        "Wingspan [cm / measure from fingertip to fingertip]: "
                    ).strip()
                )
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.wingspan <= 0:
                print("Wingspan must be greater than 0 cm")
                continue

            return self.wingspan

    def ulna_info(self):
        while True:

            try:
                self.ulna = float(
                    input("Ulna [cm / measure from elbow to wrist]: ").strip()
                )
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.ulna <= 0:
                print("Ulna must be greater than 0 cm")
                continue

            return self.ulna

    def humerus_info(self):
        while True:

            try:
                self.humerus = float(
                    input(
                        "Humerus [cm / measure from top of shoulder to elbow]: "
                    ).strip()
                )
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.humerus <= 0:
                print("Humerus must be greater than 0 cm")
                continue

            return self.humerus
