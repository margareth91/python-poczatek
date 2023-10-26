
class Student:

    def __init__(self):
        self.first_name = "Dziosia"
        self.last_name = "Dziusia"
        self.age = 18


def run_example():
    student = Student()
    print(student.first_name)
    print(student.last_name)
    print(student.age)


if __name__ == '__main__':
    run_example()


class Student:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False


def print_student(student):
    print(f"student: {student.first_name} {student.last_name}, promoted: {student.promoted}")


def promote_student(student):
    student.promoted = True


def run_example():
    student = Student(first_name="Ola", last_name="Bobak")
    print_student(student)

    other_student = Student("Jerzy", "Jurkowski")
    print_student(other_student)

    promote_student(student)
    print_student(student)


if __name__ == '__main__':
    run_example()