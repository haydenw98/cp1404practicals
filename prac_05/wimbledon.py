"""
Wimbledon
Estimate: 45 minutes
Actual: 21 minutes
"""
FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """ Main program function to read, process, and display Wimbledon data."""
    data = read_wimbledon_data(FILENAME)

    champions = count_champions(data)
    countries = extract_countries(data)

    width = max(len(champion) for champion, count in champions.items())

    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion:{width}} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def read_wimbledon_data(filename):
    """Read Wimbledon CSV file."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        next(file)
        for line in file:
            parts = line.strip().split(",")
            champion = parts[INDEX_CHAMPION]
            country = parts[INDEX_COUNTRY]
            data.append([champion, country])
    return data


def count_champions(data):
    """Count the total wins for each champion."""
    champions = {}
    for record in data:
        champion = record[0]
        try:
            champions[champion] += 1
        except KeyError:
            champions[champion] = 1
    return champions


def extract_countries(data):
    """Extracts sorted list of countries from the data."""
    countries = set()
    for record in data:
        country = record[1]
        countries.add(country)
    return sorted(countries)


main()
