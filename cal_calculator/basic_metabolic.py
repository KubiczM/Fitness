class BasicMetabolic:
    def __init__(self, sex, body_weight, height, age):
        self.basic_metabolic_rate = 0
        self.sex = sex
        self.body_weight = body_weight
        self.height = height
        self.age = age

    def basic_metabolic(self):
        if self.sex == "female":
            self.basic_metabolic_rate = 655.1 + (9.563 * self.body_weight) + (1.85 * self.height) - (4.676 * self.age)
            self.basic_metabolic_rate = round(self.basic_metabolic_rate, 2)

        elif self.sex == "male":
            self.basic_metabolic_rate = 66.5 + (13.75 * self.body_weight) + (5.003 * self.height) - (6.775 * self.age)
            self.basic_metabolic_rate = round(self.basic_metabolic_rate, 2)

        return self.basic_metabolic_rate
