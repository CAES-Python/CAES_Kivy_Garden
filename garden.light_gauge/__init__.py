"""
Light_gauge
====

The :class:`Knob` widget creates a component that looks like a
control Knob or Dial (from Wikipedia : "A control knob is a rotary
control used to provide input to a device when grasped by an
operator and turned, so that the degree of rotation corresponds to
the desired input." http://en.wikipedia.org/wiki/Control_knob).
To configure a knob a max/min, slope and step values should be provided.
Additionally, knobimg_source could be set to load
a texture that visually represents the knob.

"""
__all__     = ('Knob',)
__version__ = '0.2'

import math

from kivy.lang          import  Builder
from kivy.uix.widget    import  Widget
from kivy.properties    import  NumericProperty, ObjectProperty, StringProperty,\
	                BooleanProperty, ReferenceListProperty, BoundedNumericProperty,\
	                ListProperty
from kivy.graphics.vertex_instructions import Ellipse 
from kivy.uix.image import Image

Builder.load_string('''

<Light_gauge>
	size_hint: None, None

	canvas.before:


	Color:
		rgba: self.color
	Rectangle:
		pos: self.pos[0], self.pos[1] #pos: self.pos
		size: self.gauge_size
		do_scale: True


''')

class Light_gauge(Widget):

	min = NumericProperty(0)
	max = NumericProperty(100)

	range = ReferenceListProperty(min, max)
	value = NumericProperty(0)
	color = ListProperty([0, 1, 0, 1])
	gauge_size = ListProperty([0, 50])
	orientation = StringProperty("vertical")


	def __init__(self, *args, **kwargs):
		super(Light_gauge, self).__init__(*args, **kwargs)
		
		self.bind(pos           =   self._update)
		self.bind(size           =   self._update)


	def _update(self, *args):
		self.pos =(self.pos[0], self.pos[1])
		if self.orientation =='vertical':
			self.size = (self.size[0], self.size[1]+self.value)
		else:
			self.size = (self.size[0]+self.value, self.size[1])


