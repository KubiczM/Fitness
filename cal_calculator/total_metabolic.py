class TotalMetabolic:
    def __init__(self, activity, basic_metabolic):
        self.total_metabolic_rate = 0
        self.activity = activity
        self.basic_metabolic = basic_metabolic

    def total_metabolic(self):
        while True:
            if self.basic_metabolic:
                basic_rate = self.basic_metabolic.basic_metabolic_rate

                if self.activity == 1:
                    self.total_metabolic_rate = basic_rate * 1.4
                    self.total_metabolic_rate = round(self.total_metabolic_rate, 2)

                elif self.activity == 2:
                    self.total_metabolic_rate = basic_rate * 1.6
                    self.total_metabolic_rate = round(self.total_metabolic_rate, 2)

                elif self.activity == 3:
                    self.total_metabolic_rate = basic_rate * 1.8
                    self.total_metabolic_rate = round(self.total_metabolic_rate, 2)

                elif self.activity == 4:
                    self.total_metabolic_rate = basic_rate * 2
                    self.total_metabolic_rate = round(self.total_metabolic_rate, 2)

                return self.total_metabolic_rate
