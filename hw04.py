# ------------------------------------------------------
#        Name: Thanh Luong
#  References: Assignment 04 README and course materials
# ------------------------------------------------------
import sys

secret_word = "food"


# Task 1
def check_text():
    """Ask for a sentence until it contains the secret word, dog, or Dog."""

    while True:
        sentence = input("Give me a sentence: ")

        if secret_word in sentence:
            print("You used the secret word!")
            break

        elif "dog" in sentence or "Dog" in sentence:
            print("You used the word \"dog\" or the word \"Dog\"!")
            break

        else:
            print("Try again")


# Task 2
def check_greater():
    """Ask for two integers until they are different, then print the greater one."""

    while True:
        first = int(input("Give me a first integer: "))
        second = int(input("Give me a second integer: "))

        if first > second:
            print("First is Greater")
            break
        elif second > first:
            print("Second is Greater")
            break

        else:
            print("Try again")


# Task 3
def get_special_numbers():
    """Print odd multiples of 3 between 1 and 40 that are not multiples of 5."""

    for number in range(1, 41):

        if number % 2 == 0:
            continue

        if number % 3 != 0:
            continue

        if number % 5 == 0:
            continue

        print(number)


# Task 4.a
def my_for_loop():
    """Classify each letter in a valid string as a vowel or consonant."""

    text = input("Give me a string: ")

    if len(text) < 2 or len(text) > 5 or " " in text:
        print("bad word")
        return
    
    vowels = "aeiou"

    for letter in text:
        if letter.lower() in vowels:
            print(f"{letter} is a vowel")
        else:
            print(f"{letter} is a consonant")


# Task 4.b
def my_while_loop():
    """Repeat a menu until the user chooses b to return or c to exit."""

    while True:
        choice = input("Choose one option: a, b, or c: ")

        if choice == "a":
            continue

        elif choice == "b":
            print("Goodbye")
            return

        elif choice == "c":
            sys.exit()

        else:
            print("try again")


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")