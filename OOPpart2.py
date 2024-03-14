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
