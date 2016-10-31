#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

'''
Gauge
=====

The :class:`Gauge` widget is a widget for displaying gauge. 

.. note::

Source svg file provided for customing.

'''

__all__ = ('Gauge',)

__title__ = 'garden.gauge'
__version__ = '0.2'
__author__ = 'julien@hautefeuille.eu'

import kivy
kivy.require('1.6.0')
from kivy.config import Config
from kivy.app import App
from kivy.clock import Clock

from kivy.properties    import  NumericProperty, ObjectProperty, StringProperty,\
                                BooleanProperty, ReferenceListProperty, BoundedNumericProperty,\
                                ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
import os,inspect

class DummyClass: pass

class Gauge(Widget):
    '''
    Gauge class

    '''
    min = NumericProperty(0)
    max = NumericProperty(100)
    range = ReferenceListProperty(min, max)
    gauge_dict = {'half':'cadran.png',}
    dummy = DummyClass
    unit = NumericProperty(1.8)
    value =NumericProperty(0)
    gauge_type = StringProperty('half')
    mypath = os.path.dirname(os.path.abspath(inspect.getsourcefile(dummy)))
    file_gauge = StringProperty(mypath + os.sep + gauge_dict[gauge_type])
    file_needle = StringProperty(mypath + os.sep + "my_needle.png")
    size_gauge = BoundedNumericProperty(256, min=128, max=256, errorvalue=128)
    size_text = NumericProperty(10)

    def __init__(self, **kwargs):
        super(Gauge, self).__init__(**kwargs)
        
            
        self._gauge = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotate=False, 
            do_scale=False,
            do_translation=False
            )

        _img_gauge = Image(source=self.file_gauge, size=(self.size_gauge, 
            self.size_gauge))

        self._needle = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotate=False,
            do_scale=False,
            do_translation=False
            )

        _img_needle = Image(source=self.file_needle, size=(self.size_gauge, 
            self.size_gauge))

 #       self._glab = Label(font_size=self.size_text, markup=True)
 #       self._progress = ProgressBar(max=100, height=20, value=self.value)
       
        self._gauge.add_widget(_img_gauge)
        self._needle.add_widget(_img_needle)
        
        self.add_widget(self._gauge)
        self.add_widget(self._needle)
#        self.add_widget(self._glab)
#        self.add_widget(self._progress)

        self.bind(pos=self._update)
        self.bind(size=self._update)
        self.bind(value=self._turn)
        
    def _update(self, *args):
        '''
        Update gauge and needle positions after sizing or positioning.

        '''
        self._gauge.pos = self.pos
        self._needle.pos = (self.x, self.y)
        self._needle.center = (self._gauge.center_x, self._gauge.center_y - self._gauge.center_y/17.5)


    def _turn(self, *args):
        '''
        Turn needle, 1 degree = 1 unit, 0 degree point start on 0 value.

        '''
        self._needle.center_x = self._gauge.center_x
        self._needle.center_y = self._gauge.center_y - self._gauge.center_y/17.5
        self._needle.rotation = ( self.unit) - (self.value * self.unit)



dirflag = 1
value = 0

class GaugeApp(App):
        def build(self):
			from kivy.clock import Clock
			from functools import partial



			def setgauge(sender, value):
				mygauge.value = value
				
			def incgauge(sender, incr):
				global dirflag
				global value
				
				
				if dirflag == 1:
					if value <100:
						value += incr
						setgauge(0,value)

					else:
						dirflag = 0
				else:
					if value >0:
						value -= incr
						setgauge(sender, value)

						
					else:
						dirflag = 1
			
			mygauge = Gauge(value=0, size_gauge=256, size_text=25)
			box = BoxLayout(orientation='horizontal', spacing=5, padding=5)
			Clock.schedule_interval(partial(incgauge, incr = 1), 0.03)
			box.add_widget(mygauge)


			return box
            
if __name__ == '__main__':
    GaugeApp().run()
