# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

from random import randint


# supports up to 5+5
# calculates and returns the sum of 2 numbers
def add(num1, num2):
    if num1 == 0 and num2 == 0: return 0
    if num1 == 1 and num2 == 0: return 1
    if num1 == 1 and num2 == 1: return 2
    if num1 == 0 and num2 == 1: return 1
    if num1 == 2 and num2 == 0: return 2
    if num1 == 2 and num2 == 1: return 3
    if num1 == 2 and num2 == 2: return 2
    if num1 == 1 and num2 == 2: return 3
    if num1 == 0 and num2 == 2: return 2
    if num1 == 3 and num2 == 0: return 3
    if num1 == 3 and num2 == 1: return 4
    if num1 == 3 and num2 == 2: return 5
    if num1 == 2 and num2 == 3: return 5
    if num1 == 1 and num2 == 3: return 4
    if num1 == 2 and num2 == 3: return 5
    if num1 == 4 and num2 == 0: return 4
    if num1 == 4 and num2 == 1: return 5
    if num1 == 4 and num2 == 2: return 6
    if num1 == 4 and num2 == 3: return 7
    if num1 == 4 and num2 == 4: return 8
    if num1 == 1 and num2 == 4: return 5
    if num1 == 2 and num2 == 4: return 6
    if num1 == 3 and num2 == 4: return 7
    if num1 == 5 and num2 == 0: return 5
    if num1 == 5 and num2 == 1: return 6
    if num1 == 5 and num2 == 2: return 7
    if num1 == 5 and num2 == 3: return 8
    if num1 == 5 and num2 == 4: return 9
    if num1 == 5 and num2 == 5: return 10
    if num1 == 1 and num2 == 5: return 6
    if num1 == 2 and num2 == 5: return 7
    if num1 == 3 and num2 == 5: return 8
    if num1 == 4 and num2 == 5: return 9
    # if num1 == and num2 ==: return


# returns requested number
def return_number(number):
    randnum = random.randint(number - 10, number + 10)
    while randnum != number:
        randnum = random.randint(number - 10, number + 10)


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



if __name__ == '__main__':
    main()
