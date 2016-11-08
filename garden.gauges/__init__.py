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

import os,inspect

class DummyClass: pass

class Gauges(Widget):
    '''
    Gauge class

    '''
    min = NumericProperty(0)
    max = NumericProperty(100)
    range = ReferenceListProperty(min, max)
    gauge_dict = {'half':'white_half_gauge.png','full':'white_full_gauge.png','full':'white_3qrtrs_gauge.png'}
    needle_dict = {'black':'my_needle.png','white' :'needle.png'}
    dummy = DummyClass
    _unit = 1.8
    value =NumericProperty(0)
    gauge_type = StringProperty('half')
    needle_color = StringProperty('black')
    mypath = os.path.dirname(os.path.abspath(inspect.getsourcefile(dummy)))
    size_gauge = BoundedNumericProperty(256, min=128, max=256, errorvalue=128)
    size_text = NumericProperty(10)

    def __init__(self, **kwargs):
        super(Gauges, self).__init__(**kwargs)
        Clock.schedule_once(self._finish_init_)

    def _finish_init_(self,dt):

        if self.gauge_type == 'half':
            self._unit = 1.8
        elif self.gauge_type =='full':
            self._unit = 3.6
        elif self.gauge_type =='3/4':
             self._unit = 2.70
        else:
            raise "gauge type incorrect, ", self.gauge_type
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





