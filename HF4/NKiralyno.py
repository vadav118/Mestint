import numpy as np

class Kiralynok:
    def __init__(self,ke,c):
        self.kezdo = ke
        self.cel = c
        self.n = len(ke[0])-1


    def celteszt(self,a):
        return a[1] == self.cel

    def rakovetkezo(self,t):
        gyerekek = []
        s = t[1] - 1 #nullával való indexelés miatt
        a = t[0].copy() #
        for i in range(self.n+1):
            elofeltetel = True
            if 1 in a[:s,i]:
                elofeltetel= False

            m,k = s-1,i-1
            while m>=0 and k>=0:
                if a[m,k] == 1:
                    elofeltetel = False
                    break
                m -=1
                k -=1

            m, k = s - 1, i + 1
            while m >= 0 and k <= self.n:
                if a[m,k] == 1:
                    elofeltetel = False
                    break
                m -= 1
                k += 1

            if elofeltetel:
                uj_allpot = a.copy()
                uj_allpot[s,i] = 1
                gyerekek.append((uj_allpot,s+2))

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