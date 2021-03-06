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
__all__     = ('Light_gauge',)
__version__ = '0.1'

import math

from kivy.lang          import  Builder
from kivy.uix.widget    import  Widget
from kivy.properties    import  NumericProperty,  StringProperty,\
	                 ReferenceListProperty, BoundedNumericProperty,\
	                ListProperty
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock


class Light_gauge(Widget):

	min = NumericProperty(0)
	max = NumericProperty(100)
	range = ReferenceListProperty(min, max)
	value = NumericProperty(0)
	color = ListProperty([0, 1, 0, 1])
	gauge_size = ListProperty([100, 20])
	orientation = StringProperty("vertical")
	_old_value = -1
	_new_value = value
	def __init__(self, *args, **kwargs):
		super(Light_gauge, self).__init__(*args, **kwargs)
		with self.canvas:
			Color(rgba=self.color)
			self.rect=Rectangle(pos = self.pos, size=self.gauge_size)
		Clock.schedule_interval(self.update_rect, 0.1)
		self.bind(pos           =   self._update)
		self.bind(size           =   self._update)
		
		

	def _update(self, *args):
		
		self.pos =self.pos
		if self.orientation =='vertical':
			self.gauge_size[1] = self.value*5
		else:
			self.gauge_size[0] = self.value*5


	def update_rect(self,dt):
		if self._new_value != self._old_value:
			self.canvas.clear()
			self._update()
			with self.canvas:
				Color(rgba=self.color)
				self.rect=Rectangle(pos = self.pos, size=self.gauge_size)
			self._old_value = self._new_value 
		else:
			pass
