from keres import *
from seged import *


class Sakk_Tabla(Feladat):
    def __init__(self, ke, c):
        self.kezdő = ke
        self.cél = c

    def rákövetkező(self, állapot):
        tabla, s, o, lepes_szam = állapot
        lehetosegek = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                       (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for ls, lo in lehetosegek:
            ks, ko = s + ls, o + lo
            if 0 <= ks < 8 and 0 <= ko < 8 and tabla[ks][ko] == "0":
                uj_tabla = [list(sor) for sor in tabla]
                uj_tabla[ks][ko] = "1"
                uj_allapot = (tuple(tuple(s) for s in uj_tabla), ks, ko, lepes_szam + 1)
                yield f"lép {ks},{ko}", uj_allapot

    def célteszt(self, állapot):
        tabla, s, o, lepes_szam = állapot

        if lepes_szam != 60:
            return False


        return abs(s - 0) * abs(o - 1) == 2 or abs(s - 1) * abs(o - 0) == 2


def heurisztika(csúcs):
    állapot = csúcs.állapot
    tabla, s, o, lepes_szam = állapot
    lehetosegek = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    fokszam = 0
    for ls, lo in lehetosegek:
        ks, ko = s + ls, o + lo
        if 0 <= ks < 8 and 0 <= ko < 8 and tabla[ks][ko] == "0":
            fokszam += 1
    return fokszam


if __name__ == '__main__':
    kezdo_tabla = [["0"] * 8 for i in range(8)]
    for s, o in [(0, 0), (0, 7), (7, 0), (7, 7)]:
        kezdo_tabla[s][o] = 'x'

    kezdo_s, kezdo_o = 0, 1
    kezdo_tabla[kezdo_s][kezdo_o] = '1'

    kezdő_állapot = (tuple(tuple(i) for i in kezdo_tabla), kezdo_s, kezdo_o, 1)

    feladat = Sakk_Tabla(kezdő_állapot, None)

    # print('Szélességi gráfkereső')
    # result1 = szélességi_gráfkereső(feladat)
    # print(result1.megoldás())
    # print('Szélességi fakereső')
    # result2 = szélességi_fakereső(feladat)
    # print(result2.megoldás())
    print('Mélységi gráfkereső')
    result3 = mélységi_gráfkereső(feladat)
    print(result3.megoldás())
    print('Mélységi fakereső')
    result4 = mélységi_fakereső(feladat)
    print(result4.megoldás())

    print('Best First')
    result5 = best_first(feladat, heurisztika)
    print(result5.megoldás())
    print('A Csillag')
    result6 = a_csillag(feladat, heurisztika)
    print(result6.megoldás())