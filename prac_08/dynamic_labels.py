from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.window import Window

class DynamicLabelsApp(App):
    """Kivy App that dynamically creates Labels for a list of names."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.philosophers = ["Plato", "Aristotle", "Kant", "Nietzsche", "Beauvoir", "Schopenhauer"]

    def build(self):
        """Build the kivy app from the file"""
        self.root = Builder.load_file('dynamic_labels.kv')
        self.populate_labels()
        Window.size = (400, 300)
        return self.root

    def populate_labels(self):
        """Create and add a Label for each name in the sorted list."""
        for name in sorted(self.philosophers):
            self.add_name_label(name)

    def add_name_label(self, name):
        """Create a Label for the given name and add it to the layout."""
        label = Label(text=name, font_size=50, size_hint_y=None, height=50)
        self.root.ids.main.add_widget(label)

DynamicLabelsApp().run()