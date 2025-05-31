MENU = ("""(G)et a valid score (must be 0-100!)
(P)rint result
(S)how stars
(Q)uit""")

def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(evaluate_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you and farewell!")


def evaluate_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def get_valid_score():
    score = int(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score (0-100): "))
    return score


def show_stars(score):
    print("*" * score)

main()
