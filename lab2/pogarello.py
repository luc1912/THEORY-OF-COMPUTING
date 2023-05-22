import sys

ulazni_niz = []
ispis = []
rezultat = ""
trenutni_znak = ""


def kraj_programa():
    for i in ispis:
        print(i, end='')
    print("\n" + rezultat)
    exit()


def C():
    global ispis
    ispis.append("C")
    A()
    A()


def A():
    global trenutni_znak, ispis, ulazni_niz, rezultat
    ispis.append("A")

    if trenutni_znak not in ["a", "b"]:
        rezultat = "NE"
        kraj_programa()

    if trenutni_znak == "b":
        ulazni_niz.pop(0)
        trenutni_znak = ulazni_niz[0]
        C()
    elif trenutni_znak == "a":
        ulazni_niz.pop(0)
        trenutni_znak = ulazni_niz[0]


def B():
    global trenutni_znak, ispis, ulazni_niz, rezultat
    ispis.append("B")

    if trenutni_znak != "c":
        return

    for _ in range(2):
        if trenutni_znak != "c":
            rezultat = "NE"
            kraj_programa()

        ulazni_niz.pop(0)
        trenutni_znak = ulazni_niz[0]

    S()

    if trenutni_znak == "b":
        ulazni_niz.pop(0)
        trenutni_znak = ulazni_niz[0]
    else:
        rezultat = "NE"
        kraj_programa()

    if trenutni_znak == "c":
        ulazni_niz.pop(0)
        trenutni_znak = ulazni_niz[0]
    else:
        rezultat = "NE"
        kraj_programa()


def S():
    global trenutni_znak, ispis, ulazni_niz, rezultat
    ispis.append("S")

    if trenutni_znak not in ["a", "b"]:
        rezultat = "NE"
        kraj_programa()

    if trenutni_znak == "a":
        ulazni_niz.pop(0)
        trenutni_znak = ulazni_niz[0]
        A()
        B()
    elif trenutni_znak == "b":
        ulazni_niz.pop(0)
        trenutni_znak = ulazni_niz[0]
        B()
        A()


def main():
    global ulazni_niz, trenutni_znak, rezultat

    for line in sys.stdin:
        niz = line.rstrip()

    ulazni_niz = list(niz)
    ulazni_niz.append("KRAJ")
    trenutni_znak = ulazni_niz[0]
    S()

    if trenutni_znak != "KRAJ":
        rezultat = "NE"
        kraj_programa()
    else:
        rezultat = "DA"
        kraj_programa()


if __name__ == "__main__":
    main()
