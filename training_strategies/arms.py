class Arms:
    def __init__(self, wingspan, height):
        self.wingspan = wingspan
        self.height = height

    def arms_strategies(self):
        biceps_exercises = []
        triceps_exercises = []

        if self.wingspan > self.height:
            biceps_exercises = [
                "Barbell Curls",
                "Incline Dumbbells Curls",
                "Single Arm Preacher Curl",
                "Cable Curl",
                "Dumbbells Hammer Curl",
                "Cable Reverse Curl",
                "Machine Curl",
            ]

            triceps_exercises = [
                "JM Press",
                "Nosebreaker",
                "Overhead Dumbbell Triceps Extension",
                "Triceps Extension",
                "Rope Pressdown",
                "Decline Dumbbells Triceps Extension",
            ]

        elif self.wingspan <= self.height:
            biceps_exercises = [
                "Supinated Pull_Ups",
                "Neutral-Grip Pull Ups",
                "Barbell Curl",
                "Preacher Curl",
                "Rope Hammer Curl",
                "Cable Curl",
            ]

            triceps_exercises = [
                "Close-Grip Bench Press",
                "Dips",
                "Reverse-Grip Bench Press",
                "Nosebreaker",
                "Decline Dumbbells Triceps Extension",
                "Triceps Pressdown",
            ]

        return {"biceps": biceps_exercises, "triceps": triceps_exercises}
