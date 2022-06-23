# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

from random import randint


# returns requested number
def return_number(number):
    randnum = random.randint(number-10, number+10)
    while randnum != number:
        randnum = random.randint(number-10, number+10)



def coin_flip():
    print("Welcome to the coin flipper!")

    start = input('Press enter to flip the coin')
    count = 0
    while True:
        coin_flip = random.randint(1, 2)
        count += 1

        if count > 100:
            break

        if coin_flip == 1:
            print('Heads')

        elif coin_flip == 2:
            print("Tails")


def main():
    print('Main')
    return_number(15)


if __name__ == '__main__':
    main()
