# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Negyzet:
    def __init__(self, sides):
        self.a = sides

    def kerulet(self):
        return 4*self.a

    def terulet(self):
        return self.a ** 2


def main():
    n = Negyzet(3)
    print(f"Kerület: {n.kerulet()}")
    print(f"Terület: {n.terulet()}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
