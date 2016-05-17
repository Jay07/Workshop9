from kivy.app import App
from kivy.lang import Builder


class Convert(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('mile_convert_km.kv')
        return self.root

    def handle_convert(self):
        self.root.ids.output_km.text = str(float(self.root.ids.input_miles.text) * 1.60934)

    def handle_up(self):
        self.root.ids.input_miles.text = str(float(self.root.ids.input_miles.text) + 1)

    def handle_down(self):
        self.root.ids.input_miles.text = str(float(self.root.ids.input_miles.text) - 1)

Convert().run()