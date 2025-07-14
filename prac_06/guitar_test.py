from prac_06.guitar import Guitar
def main():
    """Run tests for guitar class"""

    Gibson = Guitar("Gibson", 1990, 250)
    Fender = Guitar("Fender", 1953, 4000)

    guitars = [Gibson, Fender]


    print(Gibson)
    print(Fender)

    for guitar in guitars:
        if guitar.is_vintage():
            print(guitar.name)

    print(f"{Gibson.name} get_age() expected 35, got {Gibson.get_age()}")
    print(f"{Fender.name} get_age() expected 72, got {Fender.get_age()}")
    print(f"{Gibson.name} is_vintage() expected False, got {Gibson.is_vintage()}")
    print(f"{Fender.name} is_vintage() expected True, got {Fender.is_vintage()}")

main()