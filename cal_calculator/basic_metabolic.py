"""
Basic Metabolic Rate Calculator

This class calculates the Basal Metabolic Rate (BMR) based on the Mifflin-St Jeor Equation.
BMR represents the number of calories required to maintain basic body functions at rest.

Class:
- BasicMetabolic: Accepts user details (sex, body weight, height, age) and calculates BMR.

Methods:
- basic_metabolic: Computes BMR based on gender-specific formulas and returns the rounded value.

Usage:
Create an instance of BasicMetabolic with the required parameters and call `basic_metabolic()` to get the BMR.
"""

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
            self.basic_metabolic_rate = round(self.basic_metabolic_rate)

        elif self.sex == "male":
            self.basic_metabolic_rate = 66.5 + (13.75 * self.body_weight) + (5.003 * self.height) - (6.775 * self.age)
            self.basic_metabolic_rate = round(self.basic_metabolic_rate)

        return self.basic_metabolic_rate
