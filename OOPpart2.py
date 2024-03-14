# Part 2
class StudentWithClass:
    def __init__(self, name, age, current_class=None):
        self.name = name
        self.age = age
        self.current_class = current_class
        self.test_scores = []

    def add_test_score(self, score):
        self.test_scores.append(score)

    def calculate_average_score(self):
        if not self.test_scores:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

# Create a student with class
student_with_class = StudentWithClass("Charlie", 19, "Math")

# Add test scores
student_with_class.add_test_score(85)
student_with_class.add_test_score(90)
student_with_class.add_test_score(88)

# Calculate average test score
print(student_with_class.calculate_average_score())
