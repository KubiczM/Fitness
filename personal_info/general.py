from personal_info.lower_limbs import LowerLimbsMeasurements
from personal_info.upper_limbs import UpperLimbsMeasurements
from cal_calculator.basic_metabolic import BasicMetabolic
from cal_calculator.total_metabolic import TotalMetabolic
from cal_calculator.cal_balance import CalBalance
from training_strategies.arms import Arms
from training_strategies.chest import Chest
from training_strategies.back import Back
from training_strategies.legs import Legs


class PersonalInfo:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.sex = ""
        self.body_weight = 0
        self.height = 0
        self.age = 0
        self.activity = 1
        self.question = 2
        self.lower_limbs = LowerLimbsMeasurements()
        self.upper_limbs = UpperLimbsMeasurements()
        self.arms = Arms(wingspan=0, height=0)
        self.chest = Chest(wingspan=0, height=0)
        self.back = Back(wingspan=0, height=0)
        self.legs = Legs(legs=0, tibia=0, height=0, femur=0)

    def update_info(self):
        self.first_name_info()
        self.last_name_info()
        self.sex_info()
        self.body_weight_info()
        self.height_info()
        self.age_info()
        print()
        self.activity_info()
        self.basic_metabolic = BasicMetabolic(self.sex, self.body_weight, self.height, self.age)
        self.total_metabolic = TotalMetabolic(self.activity, self.basic_metabolic)
        self.basic_metabolic.basic_metabolic()
        self.total_metabolic.total_metabolic()
        print()
        self.balance_cal_info()
        self.cal_balance = CalBalance(self.total_metabolic, self.question)
        self.cal_balance.balance_cal()
        print()
        self.lower_limbs.legs_info()
        self.lower_limbs.tibia_info()
        self.lower_limbs.femur_info()
        self.upper_limbs.wingspan_info()
        self.upper_limbs.ulna_info()
        self.upper_limbs.humerus_info()
        self.arms.arms_strategies()
        self.arms = Arms(wingspan=self.upper_limbs.wingspan, height=self.height)
        self.chest.chest_strategies()
        self.chest = Chest(wingspan=self.upper_limbs.wingspan, height=self.height)
        self.back.back_strategies()
        self.back = Back(wingspan=self.upper_limbs.wingspan, height=self.height)
        self.legs.legs_strategies()
        self.legs = Legs(
            legs=self.lower_limbs.legs,
            tibia=self.lower_limbs.tibia,
            height=self.height,
            femur=self.lower_limbs.femur)
        print()

        info = {
            "first name": self.first_name,
            "last name": self.last_name,
            "sex": self.sex,
            "body weight [kg]": self.body_weight,
            "height [cm]": self.height,
            "age [years]": self.age,
            "basic metabolic [cal]": self.basic_metabolic.basic_metabolic_rate,
            "total metabolic [cal]": self.total_metabolic.total_metabolic_rate,
            "calories balance [cal]": self.cal_balance.balance_cal(),
            "legs": {
                "legs [cm]": self.lower_limbs.legs,
                "tibia [cm]": self.lower_limbs.tibia,
                "femur [cm]": self.lower_limbs.femur,
            },
            "upper limbs": {
                "wingspan [cm]": self.upper_limbs.wingspan,
                "ulna [cm]": self.upper_limbs.ulna,
                "humerus [cm]": self.upper_limbs.humerus,
            },
            "arms strategy": self.arms.arms_strategies(),
            "chest strategy": self.chest.chest_strategies(),
            "back strategy": self.back.back_strategies(),
            "legs strategy": self.legs.legs_strategies(),
        }

        return info

    def first_name_info(self):
        while True:

            try:
                self.first_name = input("First name: ").strip().title()
                if not self.first_name.isalpha():
                    raise ValueError("Invalid input, must contain only letters")
                return self.first_name
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    def last_name_info(self):
        while True:

            try:
                self.last_name = input("Last name: ").strip().title()
                if not self.last_name.isalpha():
                    raise ValueError("Invalid input, must contain only letters")
                return self.last_name
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    def sex_info(self):
        while True:
            try:
                self.sex = input(
                    "Gender [female/male]: ").strip().lower()
                if not self.sex.isalpha() or self.sex not in ["female", "male"]:
                    raise ValueError("Invalid input, must contain only 'female' or 'male'")
                return self.sex
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    def body_weight_info(self):
        while True:

            try:
                self.body_weight = float(input("Body weight [kg]: ").strip())
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.body_weight <= 0:
                print("Error: Body weight must be greater than 0 kg. Please try again.")
                continue

            return self.body_weight

    def height_info(self):
        while True:

            try:
                self.height = float(input("Height [cm]: ").strip())
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.height <= 0:
                print("Error: Height must be greater than 0 cm. Please try again.")
                continue

            return self.height

    def age_info(self):
        while True:

            try:
                self.age = float(input("Age [years]: ").strip())
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.age <= 0:
                print("Error: Age must be greater than 0 years. Please try again.")
                continue

            return self.age

    def activity_info(self):
        while True:

            try:
                print(
                    "Specify your activity: 1 -> Low, 2 -> Moderate, 3 -> Active lifestyle, 4 -> Very active"
                )
                self.activity = int(
                    input("Enter a number [from the scale above]: ").strip()
                )
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.activity <= 0 or self.activity >= 5:
                print("Activity must be a number from the given scale")
                continue

            return self.activity

    def balance_cal_info(self):
        while True:

            try:
                print(
                    "Specify your calories balance: 1 -> Deficit, 2 -> N/A, 3 -> Surplus"
                )
                self.question = int(
                    input("Enter a number [from the scale above]: ").strip()
                )
            except ValueError:
                print("Error: Invalid input. Please enter a valid number.")
                continue

            if self.question <= 0 or self.activity >= 4:
                print("Calories balance must be a number from the given scale")
                continue

            return self.question
