
class Produkt:
    pass


class Zamowienie:
    pass


class Jabluszka:
    pass


class Ziemniory:
    pass


if __name__ == '__main__':
    jonagold = Jabluszka()
    papierowki = Jabluszka()
    szare_renety = Jabluszka()

    ziemniory_na_frytki = Ziemniory()
    ziemniory_na_salatke = Ziemniory()
    ziemniory_na_puree = Ziemniory()

    print("type od jonagold to:", type(jonagold))
    print("type od papierowki to:", type(papierowki))
    print("type od szare_renety to:", type(szare_renety))
    print("type od ziemniory_na_frytki to:", type(ziemniory_na_frytki))
    print("type od ziemniory_na_salatke to:", type(ziemniory_na_salatke))
    print("type od ziemniory_na_puree to:", type(ziemniory_na_puree))

    zamowienia = [Zamowienie(), Zamowienie(), Zamowienie(), Zamowienie(), Zamowienie()]
    print(zamowienia)

    lista_produktow = {
        "parowki": Produkt(),
        "bulki hot dog": Produkt(),
        "ketchup": Produkt(),
        "musztarda": Produkt(),
        "cheddar": Produkt()
    }
    print(lista_produktow)