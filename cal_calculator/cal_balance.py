class CalBalance:
    def __init__(self, total_metabolic: object, question: int) -> None:
        self.deficit_result: int = 0
        self.over_cal_result: int = 0
        self.question: int = question
        self.total_metabolic: object = total_metabolic

    def balance_cal(self) -> int:
        while True:
            if self.total_metabolic:
                total_rate: int = self.total_metabolic.total_metabolic_rate

                if self.question == 1:
                    self.deficit_result = total_rate - (total_rate * 0.15)
                    self.deficit_result = round(self.deficit_result)
                    return self.deficit_result

                elif self.question == 2:
                    total_rate = round(total_rate)
                    return total_rate

                elif self.question == 3:
                    self.over_cal_result = total_rate + (total_rate * 0.15)
                    self.over_cal_result = round(self.over_cal_result)
                    return self.over_cal_result
