class TotalMetabolic:
    def __init__(self, activity: int, basic_metabolic: object) -> None:
        self.total_metabolic_rate: int = 0
        self.activity: int = activity
        self.basic_metabolic: object = basic_metabolic

    def total_metabolic(self) -> int:
        while True:
            if self.basic_metabolic:
                basic_rate: int = self.basic_metabolic.basic_metabolic_rate

                if self.activity == 1:
                    self.total_metabolic_rate = basic_rate * 1.4
                    self.total_metabolic_rate = round(self.total_metabolic_rate)

                elif self.activity == 2:
                    self.total_metabolic_rate = basic_rate * 1.6
                    self.total_metabolic_rate = round(self.total_metabolic_rate)

                elif self.activity == 3:
                    self.total_metabolic_rate = basic_rate * 1.8
                    self.total_metabolic_rate = round(self.total_metabolic_rate)

                elif self.activity == 4:
                    self.total_metabolic_rate = basic_rate * 2
                    self.total_metabolic_rate = round(self.total_metabolic_rate)

                return self.total_metabolic_rate
