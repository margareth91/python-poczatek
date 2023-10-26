
class Student:
    pass


class Grade:
    pass


class School:
    pass


if __name__ == '__main__':
    student_dziosia = Student()

    grade_a = Grade()
    grade_f = Grade()

    my_school = School()

    print(student_dziosia)
    print(grade_a, grade_f)
    print(my_school)


print("type(student_dziosia):", type(student_dziosia))

grades = {
    1: Grade(),
    2: Grade(),
    3: Grade(),
    4: Grade(),
    5: Grade(),
    6: Grade(),
}
print(grades)

all_students = [Student(), Student(), Student()]
print(all_students)
print(all_students[0])

