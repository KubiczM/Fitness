class BasicMetabolic:
    def __init__(self, sex: str, body_weight: float, height: float, age: int) -> None:
        self.basic_metabolic_rate: int = 0
        self.sex: str = sex
        self.body_weight: float = body_weight
        self.height: float = height
        self.age: int = age

    def basic_metabolic(self) -> int:
        if self.sex == "female":
            self.basic_metabolic_rate = (655.1 + (9.563 * self.body_weight) + (1.85 * self.height)
                                         - (4.676 * self.age))
            self.basic_metabolic_rate = round(self.basic_metabolic_rate)

        elif self.sex == "male":
            self.basic_metabolic_rate = (66.5 + (13.75 * self.body_weight) + (5.003 * self.height)
                                         - (6.775 * self.age))
            self.basic_metabolic_rate = round(self.basic_metabolic_rate)

        return self.basic_metabolic_rate
