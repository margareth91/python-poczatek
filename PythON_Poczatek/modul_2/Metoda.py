
class Student:

    def __init__(self, name):
        self.name = name

    def print_something(self):
        print("To ja, metoda studenta :D")

    def print_self(self):
        print("Czym jest self? ", self)
        print("To jest dostep do name:", self.name)

    def do_all_work(self):
        print("teraz bedzie troche pracy :p")
        self.do_piece_of_work()
        self.do_piece_of_work()
        self.do_piece_of_work()
        print("kuniec :D")

    def do_piece_of_work(self):
        print("robota...")


def run_example():
    student = Student(name="Fiodus")
    student.print_something()
    student.print_self()
    student.do_all_work()


if __name__ == '__main__':
    run_example()

