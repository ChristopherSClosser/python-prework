# prints students and grades and a class average

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
    # 10% wheight
    homework = homework * 0.10
    # 30%
    quizzes = quizzes * 0.3
    # 60%
    tests = tests * 0.6
    # average for overall grade
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
    # prints out each students info
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


first_class_avg = get_class_average(first_class)
print 'Class average: %s' % first_class_avg

class_letter = get_letter_grade(first_class_avg)
print class_letter


# grade calculator
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def print_grades(grades_input):
    for grade in grades_input:
        print grade


def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
        return total


def grades_average(grades_input):
    sum_of_grades = grades_sum(grades_input)
    average = sum_of_grades / float(len(grades_input))
    return average


def grades_variance(grades):
    variance = 0
    for number in grades:
        variance += (grades_average(grades) - number) ** 2
    return variance / len(grades)


def grades_std_deviation(variance):
    return variance ** 0.5


variance = grades_variance(grades)
print_grades(grades)
print 'Sum:', grades_sum(grades)
print 'Average:', grades_average(grades)
print 'Grade variance:', grades_variance(grades)
print 'Standard deviation:', grades_std_deviation(variance)
