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