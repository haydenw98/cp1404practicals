
def main():
    """Prompts the user to enter a colour name and then displays corresponding Hex colour code.
    Case independent and repeats until user enters a blank line"""
    colour_to_hex = {"AliceBlue": "#f0f8ff", "Burgundy": "#800020", "Champagne": "#f7e7ce", "CoralPink": "#f88379",
                     "DarkLavender": "#734f96", "Eggplant": "#614051", "Fawn": "#e5aa70", "FlamingoPink": "#fc8eac",
                     "Gray": "#bebebe", "Heliotrope": "#df73ff"}

    colour_name = input("Enter a colour: ")
    while colour_name != "":
        try:
            match = next(key for key in colour_to_hex if key.casefold() == colour_name.casefold())
            print(f"{match} is {colour_to_hex[match]}.")
        except StopIteration:
            print("Invalid colour!")
        colour_name = input("Enter a colour: ")

main()