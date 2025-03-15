"""
Total Metabolic Rate Calculator

This class calculates the Total Daily Energy Expenditure (TDEE) based on activity level and Basal Metabolic Rate (BMR).

Class:
- TotalMetabolic: Uses a given BMR and activity level to estimate daily caloric needs.

Methods:
- total_metabolic:
  - Multiplies the BMR by an activity factor to determine total metabolic rate.
  - Activity levels:
    - 1: Sedentary (BMR × 1.4)
    - 2: Light activity (BMR × 1.6)
    - 3: Moderate activity (BMR × 1.8)
    - 4: Very active (BMR × 2.0)

Usage:
Create an instance of `TotalMetabolic` with a `BasicMetabolic` object and activity level (1-4).
Call `total_metabolic()` to get the estimated total caloric needs.
"""

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
