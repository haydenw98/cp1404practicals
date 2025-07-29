from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for converting miles to kilometres"""
    output_text = StringProperty()

    def build(self):
        """Build the kivy app from file"""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = ""
        return self.root

    def handle_conversion(self):
        """Handle conversion from miles to kilometres"""
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * MILES_TO_KM
            self.output_text = f"{km:.2f}km"
        except ValueError:
            self.output_text = "0.00km"

    def handle_increment(self, change):
        """Handle increment change buttons"""
        try:
            miles = float(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_conversion()


MilesConverterApp().run()