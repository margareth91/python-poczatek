
class School:

    def __init__(self, name, students=None):
        self.name = name

        if students is None:
            students = []
        self.students = students


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False


def print_student(student):
    print(f"student: {student.first_name} {student.last_name}, promoted: {student.promoted}")


def assign_student_to_school(school, student):
    school.students.append(student)


def promote_student(student):
    student.promoted = True


def create_school_with_students(school_name, number_of_students):
    students = []
    for student_number in range(number_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school


def run_example():
    school_without_students = School("Pusta szkola")
    first_student = Student(first_name="Ola", last_name="Bubak")
    assign_student_to_school(school_without_students, first_student)

    for student in school_without_students.students:
        print_student(student)


if __name__ == '__main__':
    run_example()