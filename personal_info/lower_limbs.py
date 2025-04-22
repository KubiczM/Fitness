class LowerLimbsMeasurements:
    def __init__(self) -> None:
        self.legs: float = 0.0
        self.tibia: float = 0.0
        self.femur: float = 0.0

    def legs_info(self) -> float:
        while True:
            try:
                self.legs = float(
                    input("Leg length [cm / measure from foot to hips]: ").strip()
                )
                if self.legs <= 0:
                    raise ValueError("Legs must be greater than 0 cm.")
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid number.")
                continue
            return self.legs

    def tibia_info(self) -> float:
        while True:
            try:
                self.tibia = float(
                    input("Tibia length [cm / measure from knee to ankle]: ").strip()
                )
                if self.tibia <= 0:
                    raise ValueError("Tibia must be greater than 0 cm.")
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid number.")
                continue
            return self.tibia

    def femur_info(self) -> float:
        while True:
            try:
                self.femur = float(
                    input("Femur length [cm / measure from knee to hips]: ").strip()
                )
                if self.femur <= 0:
                    raise ValueError("Femur must be greater than 0 cm.")
            except ValueError as e:
                print(f"Error: {e}. Please enter a valid number.")
                continue
            return self.femur
