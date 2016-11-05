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
__version__ = '1.2'
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
import time

class DummyClass: 
	pass

class Light(Widget):
	dummy = DummyClass
	mypath = os.path.dirname(os.path.abspath(inspect.getsourcefile(dummy)))
	Builder.load_file(mypath + os.sep +"light.kv")	
	light_color = ListProperty([1,0,0,1])
	light_size = ListProperty([50,50])


class Light_indicator2(Widget):
	'''
	Light_indicator class
	A basic Kivy example:
<Main>
BoxLayout:
	BoxLayout:
		orientation: 'vertical'
		Light_indicator:
			id:R
			num:3
			color1: 'red'
			bol1: True
			color2:'yellow'
			color3:'green'
			setting: False
			pos_l1: [25,100]
			pos_l2: [100,100]
			pos_l3: [175,100]



	BoxLayout:
		orientation: 'vertical'
		Light_indicator:
			orientation: 'vertical'
			size_lights: [50,50]
			id:Rv
			num:3
			color1: 'red'
			bol1: True
			color2:'yellow'
			color3:'green'
			setting: False
			pos_l1: [100,175]
			pos_l2: [100,100]
			pos_l3: [100,25]





	'''
	dummy = DummyClass


	mypath = os.path.dirname(os.path.abspath(inspect.getsourcefile(dummy)))
	file_setting = StringProperty(mypath + os.sep + "setting.png")
	file_setting_v = StringProperty(mypath + os.sep + "setting_v.png")
	size_setting = BoundedNumericProperty(256, min=128, max=256, errorvalue=128)
	num = NumericProperty(1)
	color_dictionary = {'red':[1,0,0,1], 'green':[0,1,0,1], 'blue':[0,0,1,1], 'yellow':[1,1,0,1], 'grey':[0.5,0.5,0.5,1]}# dictionary that calls a color and returns a RGBa list.
      
	bol1 = BooleanProperty(False) # The boolean that turns on and off the 1st light. Use the BooleanProperty if you what control in the kivy file.
	bol2 = BooleanProperty(False) # The boolean that turns on and off the 2nd light. Use the BooleanProperty if you what control in the kivy file.
	bol3 = BooleanProperty(False) # The boolean that turns on and off the 3rd light. Use the BooleanProperty if you what control in the kivy file.
	color1 = StringProperty("yellow") # name of color to refrence the dictionary. Defaults to yellow.
	color2 = StringProperty("yellow") # name of color to refrence the dictionary. Defaults to yellow.
	color3 = StringProperty("yellow") # name of color to refrence the dictionary. Defaults to yellow.
	off_color = StringProperty("grey")# name of the off_color to refrence the dictionary. Defaults to grey.
	orientation = StringProperty("horizontal") # orientation of the lights. Options are "horizontal" or "vertical".
	size_lights = ListProperty([50,50]) # size of the lights.
	setting = BooleanProperty(True) # Boolean for having a setting image or not.
	pos_l1 = ListProperty([100,100])
	pos_l2 = ListProperty([100,100])
	pos_l3 = ListProperty([100,100])
	label_on = BooleanProperty(False)
	l1_label = StringProperty("")
	l2_label = StringProperty("")
	l3_label = StringProperty("")
	text_size = NumericProperty(30)
	global _light1 
	global _light2 
	global _light3 
	global _label1 
	global _label2 
	global _label3 
	

	def __init__(self, **kwargs):
		super(Light_indicator2, self).__init__(**kwargs)
		#print 'num before init = ', self.num
		Clock.schedule_once(self._finish_init_,0.5)
		#print 'num after init = ', self.num
		Clock.schedule_once(self._finish_init_2)
		
		Clock.schedule_interval(self.my_schedule, 0.1)
		#print 'num after Clock = ', self.num

	def _finish_init_(self,dt):
		self._setting = Scatter(
			size=(self.size_setting, self.size_setting),
			do_rotate=False, 
			do_scale=True,
			do_translation=False
			)
		if self.setting == True:
			if self.orientation == 'horizontal':
				_img_setting = Image(source=self.file_setting, size=(self.size_setting, 
					self.size_setting))
				self._setting.add_widget(_img_setting)
			elif self.orientation == 'vertical':
				_img_setting = Image(source=self.file_setting_v,  size=(self.size_setting, 
					self.size_setting))
				self._setting.add_widget(_img_setting)
			else:
				raise "Invalid orientation", self.orientation
			
		
		
		if self.num  == 1:
	
			self._light1 = Light()
			self._light1.light_size = self.size_lights
			self._light1.pos = self.pos_l1
			self._setting.add_widget(self._light1)

			print 'num = ',self.num


		elif self.num  == 2:
			self._light1 = Light()
			self._light2 = Light()
			self._light1.light_size = self.size_lights
			self._light2.light_size = self.size_lights
			self._light1.pos = self.pos_l1
			self._light2.pos = self.pos_l2
			
			self._setting.add_widget(self._light1)
			self._setting.add_widget(self._light2)


			print 'num=',self.num



		elif self.num  == 3:
			self._light1 = Light()
			self._light2 = Light()
			self._light3 = Light()
			self._light1.light_size = self.size_lights
			self._light2.light_size = self.size_lights
			self._light3.light_size = self.size_lights
			self._light1.pos = self.pos_l1
			self._light2.pos = self.pos_l2
			self._light3.pos = self.pos_l3

			self._setting.add_widget(self._light1)
	
			self._setting.add_widget(self._light2)

			self._setting.add_widget(self._light3)

	
		else:

			print'#'*90
			print 'ERROR: The number of lights('+str(self.num)+ ') is not valid. Must be 1,2, or 3 lights.'
			print'#'*90
			sys.exit()

		
		self.bind(pos=self._update)
		self.bind(size=self._update)
		self.add_widget(self._setting)
	def _finish_init_2(self,dt):
	
			
		
		
		if self.num  == 1:
	
		
			if self.label_on ==True:
				self._label1= Label(text=self.l1_label, font_size = self.text_size)
				self._label1.pos = (self.label1_pos()[0], self.label1_pos()[1])
				self._setting.add_widget(self._label1)
			#print 'num = ',self.num


		elif self.num  == 2:
	
			if self.label_on ==True:

				self._label1= Label( text=self.l1_label, font_size = self.text_size)
				self._label2= Label( text=self.l2_label, font_size = self.text_size)
				self._label1.pos = (self.label1_pos()[0], self.label1_pos()[1])
				self._label2.pos = (self.label2_pos()[0], self.label2_pos()[1])	
				self._setting.add_widget(self._label1)
				self._setting.add_widget(self._label2)
			#print 'num=',self.num



		elif self.num  == 3:

			if self.label_on ==True:

				self._label1= Label( text=self.l1_label, font_size = self.text_size )
				self._label2= Label( text=self.l2_label, font_size = self.text_size )
				self._label3= Label( text=self.l3_label, font_size = self.text_size )
				self._label1.pos = (self.label1_pos()[0], self.label1_pos()[1])
				self._label2.pos = (self.label2_pos()[0], self.label2_pos()[1])	
				self._label3.pos = (self.label3_pos()[0], self.label3_pos()[1])	
				self._setting.add_widget(self._label1)
				self._setting.add_widget(self._label2)
				self._setting.add_widget(self._label3)
			#print 'num =',self.num

		

		#self.add_widget(self._setting)
		#self._setting.pos = self.pos
		self.bind(pos=self._update)
		self.bind(size=self._update)
		#self.add_widget(self._setting)

	def _update(self, *args):
		self._setting.pos = self.pos
		self._setting.size = self.size	
		if self.num  == 1:
		
			self._light1.pos = self.pos_l1
			if self.label_on ==True:
				self._label1.pos = self.label1_pos()
					
		elif self.num  == 2:

			self._light1.pos = self.pos_l1
			self._light2.pos = self.pos_l2
			if self.label_on ==True:
				self._label1.pos = self.label1_pos()
				self._label2.pos = self.label2_pos()

		elif self.num  == 3:
		
			if self.label_on ==True:
				self._label1.pos = self.label1_pos()
				self._label2.pos = self.label2_pos()
				self._label3.pos = self.label3_pos()
			self._light1.pos = self.pos_l1
			self._light2.pos = self.pos_l2
			self._light3.pos = self.pos_l3


	
	def label1_pos(self):

		if self.orientation =='horizontal':
			pos = [self.pos_l1[0],self.pos_l1[1]-50]
		else:
			pos = [self.pos_l1[0]+50,self.pos_l1[1]]
		return pos

	def label2_pos(self):
		if self.orientation =='horizontal':
			pos = [self.pos_l2[0],self.pos_l2[1]-50]
		else:
			pos = [self.pos_l2[0]+50,self.pos_l2[1]]
		return pos

	def label3_pos(self):
		if self.orientation =='horizontal':
			pos = [self.pos_l3[0],self.pos_l3[1]-50]
		else:
			pos = [self.pos_l3[0]+50,self.pos_l3[1]]
		return pos
#self.get_color()		 	
	def get_color_l1(self):
		color_rgba=self.off_color
		if self.bol1 == True:
			try:
				color_rgba = self.color_dictionary[self.color1]

			except:
				print'#'*90
				print 'ERROR: ' +self.color1 +' doesn\'t exist in the color dictionary. Add it to the __init__.py file to use that color.  '
				print'#'*90
				sys.exit()

		else:
			color_rgba = self.color_dictionary[self.off_color]
			
		
		
		return color_rgba


	def get_color_l2(self):
		color_rgba=self.off_color

		if self.bol2 == True:
			try:
				color_rgba = self.color_dictionary[self.color2]

			except:
				print'#'*90
				print 'ERROR: ' +self.color2 +' doesn\'t exist in the color dictionary. Add it to the __init__.py file to use that color.  '
				print'#'*90
				sys.exit()

		else:
			color_rgba = self.color_dictionary[self.off_color]
			
		
		
		return color_rgba


	def get_color_l3(self):
		color_rgba=self.off_color

		if self.bol3 == True:
			try:
				color_rgba = self.color_dictionary[self.color3]

			except:
				print'#'*90
				print 'ERROR: ' +self.color3 +' doesn\'t exist in the color dictionary. Add it to the __init__.py file to use that color.  '
				print'#'*90
				sys.exit()
		else:
			color_rgba = self.color_dictionary[self.off_color]
			
		
		
		return color_rgba

########################################################### Turn on/off ##############################################################
	def turn_on_off_l1(self):
		if self.bol1 == False :
			self.bol1 = True
			
		else:
			self.bol1 = False
		self.get_color_l1() 

	def turn_on_off_l2(self):
		if self.bol2 == False :
			self.bol2 = True
			
		else:
			self.bol2 = False
		self.get_color_l2() 

	def turn_on_off_l3(self):
		if self.bol3 == False:
			self.bol3 = True
			
		elif self.bol3 == True:
			self.bol3 = False
		self.get_color_l3() 

	def turn_on_off_all(self):
		if self.bol1 == False or self.bol1 == False or self.bol1 == False :
			self.bol1 = True
			self.bol2 = True
			self.bol3 = True
			
		else:
			self.bol1 = False
			self.bol2 = False
			self.bol3 = False
		self.get_color_l1()
		self.get_color_l2()
		self.get_color_l3() 
########################################################### Turn on ##############################################################
	def turn_on_l1(self):
		if self.bol1 == False :
			self.bol1 = True
		self.get_color_l1()

	def turn_on_l2(self):
		if self.bol2 == False :
			self.bol2 = True
		self.get_color_l2()

	def turn_on_l3(self):
		if self.bol3 == False :
			self.bol3 = True
		self.get_color_l3()

	def turn_on_all(self):
		if self.bol3 == False or self.bol2 == False or self.bol1 == False  :
			self.bol3 = True
			self.bol2 = True
			self.bol1 = True
		self.get_color_l3()
		self.get_color_l2()
		self.get_color_l1()
########################################################### Turn off ##############################################################
	def turn_off_l1(self):
		if self.bol1 == True :
			self.bol1 = False
		self.get_color_l1() 

	def turn_off_l2(self):
		if self.bol2 == True :
			self.bol2 = False
		self.get_color_l2() 

	def turn_off_l3(self):
		if self.bol3 == True :
			self.bol3 = False
		self.get_color_l3() 

	def turn_off_all(self):
		if self.bol3 == True or self.bol2 == True or self.bol1 == True:
			self.bol1 = False
			self.bol2 = False
			self.bol3 = False
		self.get_color_l1()
		self.get_color_l2()
		self.get_color_l3() 
################################################################# Schedule ######################################################
	def my_schedule(self,dt):
		if self.num  == 1:
			
			self._light1.light_color = self.get_color_l1()
						
		elif self.num  == 2:

			self._light1.light_color = self.get_color_l1()
			self._light2.light_color = self.get_color_l2()

		elif self.num  == 3:
			
			
			self._light1.light_color = self.get_color_l1()
			self._light2.light_color = self.get_color_l2()
			self._light3.light_color = self.get_color_l3()

			

