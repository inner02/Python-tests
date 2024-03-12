def calculate_grade(mark, level):
    if mark < 1 or mark > 100:
        return 'Error: marks must be between 1 and 100'
    
    if level == 1:
        if mark < 50:
            return 'Fail'
        elif mark <= 60:
            return 'Pass'
        elif mark <= 70:
            return 'Merit'
        else:
            return 'Distinction'
    elif level == 2:
        if mark < 40:
            return 'Fail'
        elif mark <= 50:
            return 'Pass'
        elif mark <= 65:
            return 'Merit'
        else:
            return 'Distinction'
    else:
        return 'Invalid level'

def main():
    mark = int(input("Enter the exam mark for the student (between 1 and 100): "))
    level = int(input("Enter the student level (1 or 2): "))
    
    grade = calculate_grade(mark, level)
    print("Exam grade:", grade)

if __name__ == "__main__":
    main()
