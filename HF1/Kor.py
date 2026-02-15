# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


class Kor:
    def __init__(self, radius):
        self.r =radius


    def kerulet(self):
        return 2 * self.r * math.pi


    def terulete(self):
        return self.r ** 2 * math.pi


def main():
    k = Kor(2.5)
    print(k.kerulet())
    print(k.terulete())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
