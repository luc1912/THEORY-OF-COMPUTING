import sys

# funkcija kojom tražimo epsilon okolinu nekog stanja
def epsilon_prijelazi(stanje, funkcija_prijelaza, epsilon):
    epsilon.add(stanje)
    for funkcija in funkcija_prijelaza:
        if funkcija[0] == stanje and funkcija[1] == '$':
            for i in range(2, len(funkcija)):
                if funkcija[i] != stanje and funkcija[i] not in epsilon:
                    epsilon.add(funkcija[i])
                    epsilon_prijelazi(funkcija[i], funkcija_prijelaza, epsilon)
    return epsilon


# funkcija za ispisivanje
def ispis(set) -> str:
    set = sorted(set)
    printanje = ""
    for i in set:
        printanje += i + ','
    printanje = printanje.strip(',')

    # '#' ima najmanju vrijednost po ASCII kodu pa će uvijek biti na početku
    if len(printanje) > 1 and '#' == printanje[0]:
        printanje = printanje[2:]  # da maknemo #|

    return printanje


def main():
    # prvi redak, ulazni nizovi
    ulazni_nizovi = input().split('|')
    ulazni_nizovi[-1] = ulazni_nizovi[-1].strip()
    for i in range(len(ulazni_nizovi)):
        ulazni_nizovi[i] = ulazni_nizovi[i].split(',')

    # drugi redak, skup stanja
    stanja = input().split(',')
    stanja[-1] = stanja[-1].strip()

    # treći redak, skup simbola abecede
    simboli_abecede = input().split(',')
    simboli_abecede[-1] = simboli_abecede[-1].strip()

    # četvrti red, skup prihvatljivih stanja
    prihvatljiva_stanja = input().split(',')
    prihvatljiva_stanja[-1] = prihvatljiva_stanja[-1].strip()

    # peti red, početno stanje
    poc_stanje = input().strip()

    # ostali redovi
    funkcije_prijelaza = []
    for redak in sys.stdin:  # dok ne dođemo do praznog redka
        redak = redak.replace("->", ",")
        redak = redak.split(",")
        redak[-1] = redak[-1].strip()
        funkcije_prijelaza.append(redak)

    skup_pocetnih_stanja = set()  # epsilon okolina početnog stanja pročitanog iz petog reda
    skup_pocetnih_stanja = epsilon_prijelazi(poc_stanje, funkcije_prijelaza, skup_pocetnih_stanja)

    for niz in ulazni_nizovi:
        trenutna_stanja = skup_pocetnih_stanja
        next_stanja = set()
        printanje = ispis(trenutna_stanja) + '|'
        for ulaz in niz:
            for stanje in trenutna_stanja:
                # idemo po funkcijama prijelaza i tražimo prijelaz iz ovog stanja u druga stanja
                for funkcija in funkcije_prijelaza:
                    if funkcija[0] == stanje and ulaz == funkcija[1]:
                        for i in range(2, len(funkcija)):
                            next_stanja.add(funkcija[i])  # u polje spremamo sva stanja u koje se može doći iz trenutnog
                            next_stanja = epsilon_prijelazi(funkcija[i], funkcije_prijelaza,
                                                            next_stanja)  # provjerimo epsilon prijelaze
            if len(next_stanja) == 0:
                printanje += '#|'
            else:
                printanje += ispis(next_stanja) + '|'

            # trenutna_stanja = next_stanja
            trenutna_stanja = next_stanja.copy()
            next_stanja.clear()
        print(printanje.strip('|'))


if __name__ == '__main__':
    main()