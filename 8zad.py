name = input()
bad_grades_count = 0
grades_sum = 0
class_number = 0
while bad_grades_count < 2:
    class_number += 1
    grade = float(input())
    grades_sum += grade
    if grade < 4.00:
        bad_grades_count += 1
        class_number -= 1
    if class_number == 12:
        break
if bad_grades_count != 2:
    print(f'{name} graduated. Average grade: {grades_sum/class_number:.2f}')
else:
    print(f'{name} has been excluded at {class_number + 1} grade')