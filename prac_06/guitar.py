"""guitar.py
cp1404 prac_06 - Hayden Watts
Estimate - 45 minutes
Start time - 9:45
Actual time to complete and finish time - 10:17, 32 minutes"""

CURRENT_YEAR = 2025

class Guitar:
    """Guitar class for storing information about a guitar"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """string representation of Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage"""
        vintage_age = 50
        return self.get_age() >= vintage_age
