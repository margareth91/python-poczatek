
from school import promotion_status
# mozna importowac moduly pod inna nazwa -- np. powyzszy:
# from school import promotion_status as status
# pozwala to skrocic pozniejsze odwolania --> ale: uwazac na zbyt mocne skrocenia, np do 1-3 liter etc
from school.grade_calculator import calculate_student_final_grades
from school.promote import check_promotion
from school.students_data import is_student_in_school
# from xxx import * <-- lepiej tego nie uzywac, robi sie balagan!! <-- w init.py mozna ew zdefioniowac
# co bedzie zaimportowane jesli uzyjemy 'import *' poprzez dodanie: "__all__ = ["cos"]"
# inaczej: bedzie dostepne wszystko co jest zaimportowane w pliku init.py

# ** sciezka absolutna i wzgledna
# * absolutna -- taka jak powyzej, zaczynajaca sie od source roota
# * wzgledna: "from . import xxx" --> "." == w pakiecie, w ktorym obecnie jestesmy --> wzgledem pliku, do ktorego import
# --> PEP8 zaleca sciezke absolutne

# *** skrypt startujacy:
# if __name__ == '__main__':
#     balblabla

print("witaj w elektronicznym dzienniku!")

student_name = input("Podaj imie ucznia, zeby dowiedziec sie, czy zdal/a do nastepnej klasy: ")

if not is_student_in_school(student_name):
    print(f"Niestety {student_name} nie ma na liscie")
else:
    final_grades = calculate_student_final_grades(student_name)
    promotion_result = check_promotion(final_grades)

    if promotion_result == promotion_status.PASSED:
        print(f"gratulacje! {student_name} zdal/a do nastepnej klasy :)")
    elif promotion_result == promotion_status.FAILED:
        print(f"niestety, {student_name} nie zdal/a do nastepnej klasy")
    else:
        print("cos poszlo nie tak, zglos to obsludze systemu")