"""Programming_language.py
cp1404 prac_06 - Hayden Watts
Estimate - 40 minutes
Start time - 9:15
Actual time to complete and finish time - 9:41, 26 minutes"""

class ProgrammingLanguage:
    """Represents information of a programming language."""

    def __init__(self, name="", typing="", reflection="", year=0):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if this programming language is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Display representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
