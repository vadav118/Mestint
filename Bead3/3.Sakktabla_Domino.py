from keres import *

class Dominok(Feladat):
    def __init__(self,ke ,c):
        self.kezdő = ke
        self.cél = c


    def rákövetkező(self, állapot):
        tabla, ures = állapot
        if ures <= self.cél:
            return

        s, o = -1,-1
        letezik = False
        for i in range(8):
            for j in range(8):
                if tabla[i][j] == 0:
                    s,o = i,j
                    letezik =True
                    break
            if letezik: break

        if not letezik:
            return

        if o + 2 < 8 and tabla[s][o + 1] == 0 and tabla[s][o + 2] == 0:
            uj = [list(sor) for sor in tabla]
            uj[s][o],uj[s][o+1],uj[s][o+2] = 1,1,1
            yield f"Balra néz: {s},{o}",(tuple(tuple(s) for s in uj), ures-3)

        if s + 2 < 8 and tabla[s + 1][o] == 0 and tabla[s + 2][o] == 0:
            uj = [list(sor) for sor in tabla]
            uj[s][o], uj[s + 2][o], uj[s + 2][o] = 1, 1, 1
            yield f"Lefele néz: {s},{o}", (tuple(tuple(s) for s in uj), ures - 3)

        van_ures = any(2 in sor for sor in tabla)
        if not  van_ures:
            uj = [list(sor) for sor in tabla]
            uj[s][o] = 2
            yield f"Üres fixálása: {s},{o}", (tuple(tuple(s) for s in uj), ures - 3)

    def célteszt(self, állapot):
        return állapot[1] == self.cél

def heurisztika(csúcs):
    állapot = csúcs.állapot
    return 63 - állapot[1]


if __name__ == '__main__':
    kezdo_tabla = [[0] * 8 for i in range(8)]

    kezdő_állapot = (tuple(tuple(i) for i in kezdo_tabla), 64)

    feladat = Dominok(kezdő_állapot, 1)

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
    result5 = best_first(feladat, heurisztika)
    print(result5.megoldás())
    print('A Csillag')
    result6 = a_csillag(feladat, heurisztika)
    print(result6.megoldás())