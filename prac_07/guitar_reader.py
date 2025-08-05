"""guitar_reader.py
cp1404 prac_06 - Hayden Watts
Estimate - 20 minutes
Start time - 7:30
Actual time to complete and finish time - 35 minutes, 8:15"""

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Program to load, display, and sort guitar data from csv file"""
    guitars = load_guitars(FILENAME)
    print("Here are the available guitars: ")
    display_guitars(guitars)

    print()
    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)

    print("\nHere are the available guitars in order by year: ")
    guitars.sort() # Should now work due to the __lt__ in guitar.py
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)

def load_guitars(filename):
    """Load guitars from a csv file"""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitar = Guitar(name.strip(), int(year), float(cost))
            guitars.append(guitar)
    return guitars

def get_new_guitars():
    """Get new guitars from user input to append"""
    new_guitars = []
    print("Add new guitars to list? (Press Enter to skip)")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        new_guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")
    return new_guitars

def save_guitars(filename, guitars):
    """Save guitars to a csv file"""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

def display_guitars(guitars):
    """Display the guitars in a list"""
    for index, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {index}: {guitar} {vintage_string}")

if __name__ == "__main__":
    main()

