from random import randint

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    number_of_lines = int(input('How many quick picks? '))
    for i in range(number_of_lines):
        quick_picks = []
        while len(quick_picks) < NUMBERS_PER_PICK:
            number = randint(MIN_NUMBER, MAX_NUMBER)
            if number not in quick_picks:
                quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))

main()

