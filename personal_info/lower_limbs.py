"""
Lower Limb Measurements

This class collects and stores measurements of the lower limbs,
including total leg length, tibia, and femur.

Class:
- LowerLimbsMeasurements: Manages user input for lower limb dimensions.

Methods:
- legs_info: Captures leg length from foot to hips.
- tibia_info: Captures tibia length from knee to ankle.
- femur_info: Captures femur length from knee to hips.

Usage:
Create an instance of `LowerLimbsMeasurements` and call methods to input measurements.
Values are validated to ensure correctness.
"""

class LowerLimbsMeasurements:
    def __init__(self):
        self.legs = 0
        self.tibia = 0
        self.femur = 0

    def legs_info(self):
        while True:

            try:
                self.legs = float(input("Leg length [cm / measure from foot to hips]: ").strip())
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.legs <= 0:
                print("Legs must be greater than 0 cm")
                continue

            return self.legs

    def tibia_info(self):
        while True:

            try:
                self.tibia = float(input("Tibia length [cm / measure from knee to ankle]: ").strip())
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.tibia <= 0:
                print("Tibia must be greater than 0 cm")
                continue

            return self.tibia

    def femur_info(self):
        while True:

            try:
                self.femur = float(input("Femur length [cm / measure from knee to hips]: ").strip())
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.femur <= 0:
                print("Femur must be greater than 0 cm")
                continue

            return self.femur