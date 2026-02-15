# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class FizzBuzz:
    def __init__(self, max):
        self.max = max

    def start(self):
        for i in range(1,self.max+1):
            print(self.fizz_buzz(i))

    def fizz_buzz(self, i):
        if i % 3 == 0 and i % 5 == 0:
            return "FizzBuzz"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"
        else:
            return i


def main():
   n = int(input("Adj meg egy számot: "))
   f = FizzBuzz(n)
   f.start()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

