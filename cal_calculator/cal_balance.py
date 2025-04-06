"""
Caloric Balance Calculator

This class calculates daily caloric needs based on total metabolic rate and user goals.

Class:
- CalBalance: Determines caloric intake based on whether the user wants a caloric deficit, maintenance, or surplus.

Methods:
- balance_cal:
  - Option 1: Returns a 15% caloric deficit.
  - Option 2: Returns the maintenance caloric intake.
  - Option 3: Returns a 15% caloric surplus.

Usage:
Create an instance of `CalBalance` with the total metabolic rate and a goal selection (1, 2, or 3).
Call `balance_cal()` to get the recommended caloric intake.
"""


class CalBalance:
    def __init__(self, total_metabolic, question):
        self.deficit_result = 0
        self.over_cal_result = 0
        self.question = question
        self.total_metabolic = total_metabolic

    def balance_cal(self):
        while True:
            if self.total_metabolic:
                total_rate = self.total_metabolic.total_metabolic_rate

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
