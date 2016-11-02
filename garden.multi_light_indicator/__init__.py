#!/usr/bin/env python


'''
Multi-Light indicator
=====

The :class:`Light_indicator` widget is a widget for displaying Light_indicator. 

.. note::



'''
# This is the dictionary which maps the user color choice to the rgba list property.

__all__ = ('Multi_light_indicator',)

__title__ = 'garden.multi_light_indicator'
__version__ = '0.1'
__author__ = 'Marcus Holden'
# shoutout to julien@hautefeuille.eu and the creator of the kivy garden knobs, whose __init__.py code helped me develop this file.
import kivy
kivy.require('1.9.1')
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock
from kivy.lang  import  Builder

from kivy.properties    import   StringProperty, BooleanProperty, ReferenceListProperty, ListProperty, StringProperty, BoundedNumericProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics.vertex_instructions import Ellipse, Rectangle
from kivy.graphics.context_instructions import Color
from functools import partial
import os,inspect,sys

class DummyClass: 
	pass

class Light(Widget):
	dummy = DummyClass
	mypath = os.path.dirname(os.path.abspath(inspect.getsourcefile(dummy)))
	Builder.load_file(mypath + os.sep +"light.kv")	
	light_color = ListProperty([1,0,0,1])
	light_size = ListProperty([50,50])



class Multi_light_indicator(Widget):
	'''
	Light_indicator class
	A basic Kivy example:
BoxLayout:
	BoxLayout:
		orientation: 'vertical'
		Light_indicator:
			id:R
			color: 'red'
		Light_indicator:
			id:G
			color: 'green'
		Light_indicator:
			id:B
			color: 'blue'
			off_color: 'red'
		Light_indicator:
			id:P
			color: 'purple'

	BoxLayout:
		orientation: 'vertical'	
		Button:
			text: 'R'
			on_release:R.turn_on_off()
		Button:
			text: 'G'
			on_release:G.turn_on_off()

		Button:
			text: 'B'
			on_release:B.turn_on_off()
		Button:
			text: 'P'
			on_release:P.turn_on_off()

NOTE: Since 'purple' is not currently found in the color_dictionary of this file, an exception is raised and the program exits when the button is pressed. 
	'''
	dummy = DummyClass
	mypath = os.path.dirname(os.path.abspath(inspect.getsourcefile(dummy)))
	file_setting = StringProperty(mypath + os.sep + "setting.png")
	size_setting = BoundedNumericProperty(256, min=128, max=256, errorvalue=128)
	num = BoundedNumericProperty(3, min=1, max=3, errorvalue=1)
	color_dictionary = {'red':[1,0,0,1], 'green':[0,1,0,1], 'blue':[0,0,1,1], 'yellow':[1,1,0,1], 'grey':[0.5,0.5,0.5,1]}# dictionary that calls a color and returns a RGBa list.
      
	_bol = False #BooleanProperty(False) # The boolean that turns on and off the light. Use the BooleanProperty if you what control in the kivy file.
	color1 = StringProperty("yellow") # name of color to refrence the dictionary. Defaults to yellow.
	color2 = StringProperty("yellow") # name of color to refrence the dictionary. Defaults to yellow.
	color3 = StringProperty("yellow") # name of color to refrence the dictionary. Defaults to yellow.
	off_color = StringProperty("grey")# name of the off_color to refrence the dictionary. Defaults to grey.

	

	def __init__(self, **kwargs):
		super(Multi_light_indicator, self).__init__(**kwargs)
		self._light1 = Light()
		self._light2 = Light()
		self._light3 = Light()
		self._setting = Scatter(
			size=(self.size_setting, self.size_setting),
			do_rotate=False, 
			do_scale=True,
			do_translation=False
			)
		_img_setting = Image(source=self.file_setting, size=(self.size_setting, 
			self.size_setting))
		self._setting.add_widget(_img_setting)


		if self.num  == 1:
			
			
			self._light1.pos = (100 ,100)
			self._light2.pos = (100 ,100)
			self._light3.pos = (100 ,100)
			self._setting.add_widget(self._light3)
			self._setting.add_widget(self._light2)
			self._setting.add_widget(self._light1)
			print 'num = ',self.num
		elif self.num  == 2:
			
			self._light1.pos = (50,100)
			self._light1.pos = (50,100)
			self._light2.pos = (150,100)
			self._setting.add_widget(self._light3)			
			self._setting.add_widget(self._light1)
			self._setting.add_widget(self._light2)
			print 'num=',self.num
		elif self.num  == 3:
			
			self._light1.pos = (25 ,100)
			self._light2.pos = (100,100)
			self._light3.pos = (175,100)
			self._setting.add_widget(self._light1)
			self._setting.add_widget(self._light2)
			self._setting.add_widget(self._light3)
			print 'num =',self.num
		else:
			print 'the number of lights is not valid.'
			sys.exit()

		self.add_widget(self._setting)
		
		self.bind(pos=self._update)
		self.bind(size=self._update)
		Clock.schedule_interval(self.my_schedule, 0.1)
		

	def _update(self, *args):
		
		self._setting.pos = self.pos
		self._setting.size = self.size
		
			
		if self.num  == 1:
			
			self._light1.pos = (100 ,100)
						
		elif self.num  == 2:

			self._light1.pos = (50,100)
			self._light2.pos = (150,100)

		elif self.num  == 3:
			
			self._light1.pos = (25 ,100)
			self._light2.pos = (100,100)
			self._light3.pos = (175,100)
		else:
			print 'the number of lights is not valid.'
			sys.exit()
#self.get_color()
		
	def get_color(self):
		color_rgba=self.off_color
		if self._bol == True:
			try:
				color_rgba = [self.color_dictionary[self.color1],self.color_dictionary[self.color2],self.color_dictionary[self.color3]]

			except:
				print 'ERROR: Your color doesn\'t exist in the dictionary. Add it to the __init__.py file to use that color.  '
				sys.exit()
		else:
			color_rgba = [self.color_dictionary[self.off_color],self.color_dictionary[self.off_color],self.color_dictionary[self.off_color]]
			
		
		print color_rgba
		return color_rgba


	def turn_on_off(self):
		if self._bol == False :
			self._bol = True
			
		else:
			self._bol = False
		self.get_color() 

	def turn_on(self):
		if self._bol == False :
			self._bol = True
		self.get_color()

	def turn_off(self):
		if self._bol == True :
			self._bol = False
		self.get_color() 

	def my_schedule(self,dt):
		if self.num  == 1:
			
			self._light1.light_color = self.get_color()[0]
						
		elif self.num  == 2:

			self._light1.light_color = self.get_color()[0]
			self._light2.light_color = self.get_color()[1]

		elif self.num  == 3:
			
			
			self._light1.light_color = self.get_color()[0]
			self._light2.light_color = self.get_color()[1]
			self._light3.light_color = self.get_color()[2]

			

