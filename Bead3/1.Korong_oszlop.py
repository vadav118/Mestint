from keres import *
from seged import *

class Korongok(Feladat):
    def __init__(self,ke,c):
        self.cél = c
        self.kezdő = ke
        self.N = len(ke)

    def rákövetkező(self, állapot):
        gyerekek = []
        l = list(állapot)
        for i in range(2,self.N+1):
            tmp = l[:]
            muvelet = f'megfordit {tmp[i-1]} '

            leemelt = tmp[:i]
            megforditott = leemelt[::-1]
            uj_sorrend = megforditott + tmp[i:]

            gyerekek.append((muvelet,tuple(uj_sorrend)))
        return gyerekek

    def célteszt(self, állapot):
        return self.cél == állapot

def heurisztika(csúcs):
    állapot = csúcs.állapot
    hiba = 0
    for i in range(len(állapot) - 1):
        if abs(állapot[i] - állapot[i + 1]) != 1:
            hiba += 1

    if állapot[-1] != len(állapot):
        hiba += 1

    return hiba


if __name__ == "__main__":
    feladat = Korongok((6,7,3,2,8,5,4,1),(1,2,3,4,5,6,7,8))
    print('Szélességi gráfkereső')
    result1 = szélességi_gráfkereső(feladat)
    print(result1.megoldás())
    print('Szélességi fakereső')
    result2 = szélességi_fakereső(feladat)
    print(result2.megoldás())
    print('Mélységi gráfkereső')
    result3 = mélységi_gráfkereső(feladat)
    print(result3.megoldás())
    print('Mélységi fakereső')
    result4 = mélységi_fakereső(feladat)
    print(result4.megoldás())

    print('Best First')
    result5 = best_first(feladat,heurisztika)
    print(result5.megoldás())
    print('A Csillag')
    result6 = a_csillag(feladat, heurisztika)
    print(result6.megoldás())
