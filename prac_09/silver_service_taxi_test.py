from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test SilverServiceTaxi with 18km drive and fare check."""
    taxi = SilverServiceTaxi("Silver Service Taxi", 100, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    print(taxi)
    test_fare(fare)


def test_fare(fare):
    """Test fare check."""
    expected_fare = 48.80
    print(f"Calculated fare: ${fare:.2f}")
    assert abs(fare - expected_fare) < 0.01, f"Expected fare to be ${expected_fare} - received ${fare:.2f}"


main()