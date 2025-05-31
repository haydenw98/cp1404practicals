from random import randint

def main():
    score = float(input("Enter score: "))
    print(evaluate_score(score))
    print(evaluate_score(randint(1, 100)))


def evaluate_score(score):
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()