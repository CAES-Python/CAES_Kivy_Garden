#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4 nu

'''
Gauges
=====

The :class:`Gauges` widget is a widget for displaying gauge. 

.. note::

Source svg file provided for customing.

'''

__all__ = ('Gauge',)

__title__ = 'garden.gauges'
__version__ = '0.1'
__author__ = 'makasuh@gmail.com'
# Modified from the code created by julien@hautefeuille.eu
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

import os,inspect, sys

class DummyClass: pass

class Gauges(Widget):
    '''
    Gauge class

    '''
    min = NumericProperty(0)
    max = NumericProperty(100)
    range = ReferenceListProperty(min, max)
    gauge_dict = {'half':'white_half_gauge.png','full':'white_full_gauge.png','3/4':'white_3qrtrs_gauge.png','60':'white_60_gauge.png'}
    needle_dict = {'black':'my_needle.png','white' :'needle.png','3/4':'my_34needle.png','60':'my_60needle.png'}
    dummy = DummyClass
    _unit = 1.8
    value =NumericProperty(0)
    gauge_type = StringProperty('half')
    needle_type = StringProperty('black')
    mypath = os.path.dirname(os.path.abspath(inspect.getsourcefile(dummy)))
    size_gauge = BoundedNumericProperty(256, min=128, max=256, errorvalue=128)
    size_text = NumericProperty(10)

    def __init__(self, **kwargs):
        super(Gauges, self).__init__(**kwargs)
        Clock.schedule_once(self._finish_init_,0.5)

    def _finish_init_(self,dt):

        if self.gauge_type == 'half':
            self._unit = 1.8
            self.needle_type ='black'
        elif self.gauge_type =='full':
            self._unit = 3.6
            self.needle_type ='black'
        elif self.gauge_type =='3/4':
            self._unit = 2.71
            self.needle_type ='3/4'
        elif self.gauge_type =='60':
            self._unit = 1.45
            self.needle_type ='60'
        else:
            print "#" *60
            print "#" *60
            print "ERROR: Gauge type incorrect! Add the image to the dictionary found in the __init__.py file."
            print "#" *60
            print "#" *60
            sys.exit()
        self._gauge = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotate=False, 
            do_scale=False,
            do_translation=False
            )

        _img_gauge = Image(source=self.mypath + os.sep + self.gauge_dict[self.gauge_type], size=(self.size_gauge, 
            self.size_gauge))

        self._needle = Scatter(
            size=(self.size_gauge, self.size_gauge),
            do_rotate=False,
            do_scale=False,
            do_translation=False
            )

        _img_needle = Image(source=self.mypath + os.sep + self.needle_dict[self.needle_type], size=(self.size_gauge, 
            self.size_gauge))

       
        self._gauge.add_widget(_img_gauge)
        self._needle.add_widget(_img_needle)
        
        self.add_widget(self._gauge)
        self.add_widget(self._needle)


        self.bind(pos=self._update)
        self.bind(size=self._update)
        self.bind(value=self._turn)
        
    def _update(self, *args):
        '''
        Update gauge and needle positions after sizing or positioning.

        '''
        if self.gauge_type =='half':        
            self._gauge.pos = self.pos
            self._needle.pos = (self.x, self.y)
            self._needle.center = (self._gauge.center_x, self._gauge.center_y-60)
        elif self.gauge_type =='full':        
            self._gauge.pos = self.pos
            self._needle.pos = (self.x, self.y)
            self._needle.center = (self._gauge.center_x, self._gauge.center_y)
        elif self.gauge_type =='3/4':        
            self._gauge.pos = self.pos
            self._needle.pos = (self.x, self.y)
            self._needle.center = (self._gauge.center_x, self._gauge.center_y)
        elif self.gauge_type =='60':        
            self._gauge.pos = self.pos
            self._needle.pos = (self.x, self.y)
            self._needle.center = (self._gauge.center_x, self._gauge.center_y-60)

    def _turn(self, *args):
        '''
        Turn needle, 1 degree = 1 unit, 0 degree point start on 0 value.

        '''
        if self.gauge_type =='half':
            self._needle.center_x = self._gauge.center_x
            self._needle.center_y = self._gauge.center_y-60
            self._needle.rotation = ( self._unit) - (self.value * self._unit)
        elif self.gauge_type =='full':
            self._needle.center_x = self._gauge.center_x
            self._needle.center_y = self._gauge.center_y
            self._needle.rotation = ( self._unit) - (self.value * self._unit)
        elif self.gauge_type =='3/4':
            self._needle.center_x = self._gauge.center_x
            self._needle.center_y = self._gauge.center_y
            self._needle.rotation = ( self._unit) - (self.value * self._unit)
        elif self.gauge_type =='60':
            self._needle.center_x = self._gauge.center_x
            self._needle.center_y = self._gauge.center_y-60
            self._needle.rotation = ( self._unit) - (self.value * self._unit)

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
			
			mygauge = Gauges(value=0, size_gauge=256, size_text=25, gauge_type= '3/4')
            #mygauge2 = Gauges(value=0, size_gauge=256, size_text=25, gauge_type= 'half')
			box = BoxLayout(orientation='horizontal', spacing=5, padding=5)
			Clock.schedule_interval(partial(incgauge, incr = 1), 0.03)
			box.add_widget(mygauge)
            #box.add_widget(mygauge2)


			return box
            
if __name__ == '__main__':
    GaugeApp().run()

