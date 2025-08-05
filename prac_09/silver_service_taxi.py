from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A more luxurious version of a Taxi with a flagfall and fanciness multiplier."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with name, fuel, and fanciness level."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Calculate fare including base fare and additional flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string representation of SilverServiceTaxi including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
