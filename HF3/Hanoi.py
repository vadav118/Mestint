class Hanoi:
    def init(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel

    def celtest(self, a):
        return a == self.cel

    def rakovetkezo(self, a):
        gyerekek = []
        for melyikrol in range(3):
            for hova in range(3):
                if melyikrol == hova or not a[melyikrol]:
                    continue

                uj_allapot = [list(r) for r in a]
                korong = uj_allapot[melyikrol][0]  # min

                if not uj_allapot[hova] or korong < uj_allapot[hova][0]:
                    uj_allapot[melyikrol].pop(0)
                    uj_allapot[hova].insert(0, korong)
                    gyerekek.append(tuple(uj_allapot))

        return gyerekek




if __name__ == "main":
    feladat = Hanoi(([1,2,3,4,5],[],[]),([],[],[1,2,3,4,5]))