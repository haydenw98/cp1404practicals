"""guitar_reader.py
cp1404 prac_06 - Hayden Watts
Estimate - 20 minutes
Start time - 7:30
Actual time to complete and finish time - """

from prac_07.guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Program to load, display, and sort guitar data from csv file"""
    guitars = load_guitars(FILENAME)
    print("Here are the available guitars: ")
    display_guitars(guitars)
    print("\nHere are the available guitars in order by year: ")
    guitars.sort() # Should now work due to the __lt__ in guitar.py
    display_guitars(guitars)

def load_guitars(filename):
    """Load guitars from a csv file"""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitar = Guitar(name.strip(), int(year), float(cost))
            guitars.append(guitar)
    return guitars

def display_guitars(guitars):
    """Display the guitars in a list"""
    for index, guitar in enumerate(guitars, 1):
        print(f"Guitar {index}: {guitar}")

main()

