from kivy.base  import  runTouchApp
from kivy.lang  import  Builder
from kivy.garden.toggle_knob import  Toggle_knob

# LOAD KV UIX
runTouchApp(Builder.load_file('example.kv'))
