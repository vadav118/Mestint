import numpy as np

class Kiralynok:
    def __init__(self,ke,c):
        self.kezdo = ke
        self.cel = c
        self.n = len(ke[0])


    def celteszt(self,a):
        return a[1] == self.cel

    def rakovetkezo(self,t):
        gyerekek = []
        s = t[1]
        a = t[0].copy() #
        for i in range(1,self.n+1):
            elofeltetel = True
            if 1 in a[:s-1,i-1]:
                elofeltetel= False

            if elofeltetel:
                for m in range(1,s):
                    for k in range(1,self.n+1):
                        if a[m-1, k-1] == 1 and abs(m-s) == abs(k-i):
                            elofeltetel = False
                            break
                    if not elofeltetel:
                        break

            if elofeltetel:
                uj_allpot = a.copy()
                uj_allpot[s-1,i-1] = 1
                gyerekek.append((uj_allpot,s+1))

        return gyerekek

if __name__ == '__main__':

    tabla = np.zeros((8,8), dtype=int)

    feladat = Kiralynok((tabla,1),9)

    allapotok = [feladat.kezdo]

    while allapotok:
        uj = []
        for a in allapotok:
            if feladat.celteszt(a):
                print(a[0])
                exit()
            uj += feladat.rakovetkezo(a)
        allapotok = uj