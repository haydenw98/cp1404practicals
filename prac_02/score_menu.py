MENU = ("""(G)et a valid score (must be 0-100!)
        (P)rint result
        (S)how stars
        (Q)uit""")

def main():
    print(MENU)
    choice = input(">>>: ").upper()
    while choice != "Q":
        if choice == "G":
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid choice")
        choice = input(">>>: ").upper()
    print("Thank you and farewell!")


main()
