class UpperLimbsMeasurements:
    def __init__(self) -> None:
        self.wingspan: float = 0.0
        self.ulna: float = 0.0
        self.humerus: float = 0.0

    def wingspan_info(self) -> float:
        while True:
            try:
                self.wingspan = float(input("Wingspan [cm / measure from fingertip to fingertip]: ").strip())
                if self.wingspan <= 0:
                    print("Wingspan must be greater than 0 cm")
                    continue
                return self.wingspan
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

    def ulna_info(self) -> float:
        while True:
            try:
                self.ulna = float(input("Ulna [cm / measure from elbow to wrist]: ").strip())
                if self.ulna <= 0:
                    print("Ulna must be greater than 0 cm")
                    continue
                return self.ulna
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

    def humerus_info(self) -> float:
        while True:
            try:
                self.humerus = float(input("Humerus [cm / measure from top of shoulder to elbow]: ").strip())
                if self.humerus <= 0:
                    print("Humerus must be greater than 0 cm")
                    continue
                return self.humerus
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue
