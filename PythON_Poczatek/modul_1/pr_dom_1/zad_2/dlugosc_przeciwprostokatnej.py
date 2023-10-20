
import math

def dlugosc_przeciwprostokatnej(a, b):
    # print("Obliczam dlugosc przeciwprostokatnej")
    # a = int(input("Podaj dlugosc pierwszej przyprostokatnej (w cm): "))
    # b = int(input("Podaj dlugosc drugiej przyprostokatnej (w cm): "))
    c = math.sqrt((math.pow(a, 2)) + (math.pow(b, 2)))
    print(f"Dlugosc przeciwprostokatnej to {c:.0f} cm2.")

a = int(input("Podaj dlugosc pierwszej przyprostokatnej (w cm): "))
b = int(input("Podaj dlugosc drugiej przyprostokatnej (w cm): "))

dlugosc_przeciwprostokatnej(a, b)