lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}


def average(numbers):
    total = 0
    total = sum(numbers)
    total = float(total) / len(numbers)
    return total


def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    homework = homework * 0.10
    quizzes = quizzes * 0.3
    tests = tests * 0.6
    total = homework + quizzes + tests
    return total


def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


first_class = [lloyd, alice, tyler]

for student in first_class:
    first_quarter = get_average(student)
    print student['name']
    print first_quarter
    print get_letter_grade(first_quarter)
    print


def get_class_average(class_list):
    results = []
    for student in class_list:
        grade = get_average(student)
        results.append(grade)
        class_avg = average(results)
        return class_avg


print 'Class average: %s' % get_class_average(first_class)
