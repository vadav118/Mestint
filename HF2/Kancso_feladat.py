class KancsoFeladat:
    def __init__(self, ke, c):
        self.kezdo = ke
        self.c = c
        self.Max1 = 3
        self.Max2 = 5
        self.Max3 = 8


    def celteszt(self, a):
        #return self.c in a
        return a[0] == self.c or a[1] == self.c or a[2] == self.c


    def rakovetkezo(self,a):
        gyerekek = []
        a1,a2,a3 = a

        # 1->2
        if a1 != 0 and a2 != self.Max2:
            T = min(a1,self.Max2-a2)
            gyerekek.append(("1->2",(a1 - T, a2 + T, a3)))

        # 1->3
        if a1 != 0 and a3 != self.Max3:
            T = min(a1,self.Max3-a3)
            gyerekek.append(("1->3",(a1 - T, a2, a3 + T)))

        # 2->1
        if a2 != 0 and a1!= self.Max1:
            T = min(a2,self.Max1-a1)
            gyerekek.append(("1->3",(a1 + T, a2 - T, a3)))

        # 2->3
        if a2 != 0 and a3!= self.Max3:
            T = min(a2,self.Max3-a3)
            gyerekek.append(("1->3",(a1, a2 - T, a3 + T)))

        # 3->1
        if a3 != 0 and a1!= self.Max1:
            T = min(a3,self.Max1-a1)
            gyerekek.append(("1->3",(a1 + T, a2, a3 - T)))

        # 3->2
        if a3 != 0 and a2!= self.Max2:
            T = min(a3,self.Max2-a2)
            gyerekek.append(("1->3",(a1, a2 + T, a3 - T)))

        return gyerekek





if __name__ == '__main__':
    feladat = KancsoFeladat((0,0,8),4)

    kancso = feladat.kezdo
    visited = {kancso}

    while not feladat.celteszt(kancso):
        operations = feladat.rakovetkezo(kancso)

        for text, state in operations:
            if state not in visited:
                kancso = state
                visited.add(state)
                print(text, "->",kancso)
                break

    print("Megoldas: ", kancso)