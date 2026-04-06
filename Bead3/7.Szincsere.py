from keres import *
from seged import *


class SzinCsere(Feladat):
    def __init__(self, ke, c):
        self.kezdő = ke
        self.cél = c
        self.szomszedok = {
            0: [1], 1: [0, 2, 3], 2: [1],
            3: [1, 5],
            4: [5], 5: [3, 4, 6],
            6: [5, 8],
            7: [8], 8: [6, 7, 9], 9: [8]
        }

    def rákövetkező(self, állapot):
        l = list(állapot)
        ures_helyek = [i for i, x in enumerate(l) if x == "u"]

        for ures in ures_helyek:
            for szomszed in self.szomszedok[ures]:
                if l[szomszed] != "u":
                    uj_l = l[:]
                    uj_l[ures], uj_l[szomszed] = uj_l[szomszed], uj_l[ures]
                    szin = "zöld" if l[szomszed] == "z" else "piros"
                    muvelet = f"{szin} mozgatása: {szomszed} -> {ures}"
                    yield muvelet, tuple(uj_l)

    def célteszt(self, állapot):
        return állapot == self.cél


def heurisztika(csúcs):
    aktualis = csúcs.állapot
    cel = feladat.cél
    hiba = 0
    for i in range(len(aktualis)):
        if aktualis[i] != "u" and aktualis[i] != cel[i]:
            hiba += 1
    return hiba


if __name__ == "__main__":
    kezdő = (
        "z", "z", "z",
             "u",
        "u", "u",
             "u",
        "p", "p", "p"
    )

    cél = (
        "p", "p", "p",
             "u",
        "u", "u",
             "u",
        "z", "z", "z"
    )

    feladat = SzinCsere(kezdő, cél)

    print('Szélességi gráfkereső')
    result1 = szélességi_gráfkereső(feladat)
    print(result1.megoldás())
    # print('Szélességi fakereső')
    # result2 = szélességi_fakereső(feladat)
    # print(result2.megoldás())
    print('Mélységi gráfkereső')
    result3 = mélységi_gráfkereső(feladat)
    print(result3.megoldás())
    # print('Mélységi fakereső')
    # result4 = mélységi_fakereső(feladat)
    # print(result4.megoldás())

    print('Best First')
    result5 = best_first(feladat, heurisztika)
    print(result5.megoldás())
    print('A Csillag')
    result6 = a_csillag(feladat, heurisztika)
    print(result6.megoldás())