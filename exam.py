def calculate_grade(mark):
    if mark < 1 or mark > 100:
        return 'Error: marks must be between 1 and 100'
    elif mark < 50:
        return 'Fail'
    elif mark <= 60:
        return 'Pass'
    elif mark <= 70:
        return 'Merit'
    else:
        return 'Distinction'

def main():
    mark = int(input("Enter the exam mark for the student (between 1 and 100): "))
    grade = calculate_grade(mark)
    print("Exam grade:", grade)


main()
