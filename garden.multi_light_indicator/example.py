#example
from kivy.base  import  runTouchApp
from kivy.lang  import  Builder
from kivy.garden.multi_light_indicator import  Multi_light_indicator
from kivy.uix.button import Button

# LOAD KV UIX
runTouchApp(Builder.load_file('example.kv'))