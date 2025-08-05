from prac_09.unreliable_car import UnreliableCar

def main():
    """Test unreliable car class with 2 cars with different reliability values."""
    car_one = UnreliableCar("Ol' Faithful", 150, 80)
    car_two = UnreliableCar("Deathtrap", 150, 20)

    attempts = 15

    for i in range(1, attempts + 1):
        print(f"Test attempt {i}:")
        print(f"{car_one.name:14} drove {car_one.drive(i)}km")
        print(f"{car_two.name:14} drove {car_two.drive(i)}km")

    print("\nFinal states:")
    print(car_one)
    print(car_two)


main()