from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.garden.light_gauge import Light_gauge
from kivy.garden.knob import Knob

class My_Layout(BoxLayout):
	pass

class ExampleApp(App):
	def build(self):
		return My_Layout()
# Run the program
if __name__ == "__main__":
	ExampleApp().run()
