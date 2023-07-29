"""
1. main function
2. Word List


"""
import random

WORD_LI = ["Poland", "United states of America", "India", "Russia", "France"]


def game():
    cus_li = WORD_LI.copy()
    my_word = random.choice(cus_li)
    cus_li.remove(my_word)
    length = len(my_word)
    for _ in range(length):
        print("_", end=" ")
    return ""


def main():
    print("Hello, welcome to hangman game.")
    answer = input("Press c to continue and q to quit. ")
    if answer == 'c':
        pass
    elif answer == 'q':
        return "You have quit."
    else:
        print("Invalid answer.")
    print(game())


main()
