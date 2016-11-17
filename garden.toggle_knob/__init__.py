"""
    Knob
    ====

    The :class:`Knob` widget creates a component that looks like a
    control Knob or Dial (from Wikipedia : "A control knob is a rotary
    control used to provide input to a device when grasped by an
    operator and turned, so that the degree of rotation corresponds to
    the desired input." http://en.wikipedia.org/wiki/Control_knob).
    To configure a knob a max/min, slope and step values should be provided.
    Additionally, file_knob could be set to load
    a texture that visually represents the knob.

"""
__all__     = ('Toggle_knob',)
__version__ = '0.2'

import math

from kivy.lang          import  Builder
from kivy.uix.widget    import  Widget
from kivy.properties    import  NumericProperty, ObjectProperty, StringProperty,\
                                BooleanProperty, ReferenceListProperty, BoundedNumericProperty,\
                                ListProperty
from kivy.graphics.vertex_instructions import Ellipse 
from kivy.uix.image import Image


import os,inspect,sys


Builder.load_string('''
#
#    Knob
#    ====
#     To create a basic knob (in a kv file):
#
#     Knob:
#       size:               100, 100
#       min:                0
#       max:                100
#       step:               1
#       slope:              1
#       value:              0                       # Default position of knob.
#       file_knob:     "img/knob_metal.png"    # Knob texture
#       show_marker:        False                   # Do not show surrounding marker
#
#     To create a knob with a surrounding marker:
#
#     Knob:
#       size:               100, 100
#       min:                0
#       max:                100
#       step:               1
#       slope:              1
#       value:              0                       # Default position of knob.
#       file_knob:     "img/knob_metal.png"    # Knob texture
#       show_marker:        True                    # Show surrounding marker
#       marker_img:         "img/bline.png"         # Marker texture image
#       knob_size:          0.9                     # Scales knob size to leave space for marker
#       markeroff_color:    0, 0, 0, 0

# 
<Toggle_knob>
    size_hint: None, None

    canvas.before:

        Ellipse:
            pos: self.pos[0]self.size[0] * (1 - self.knobimg_size))/2, self.pos[1] + (self.size[1] * (1 - self.knobimg_size)) / 2
            size: self.size * (self.knobimg_size), self.size * (self.knobimg_size) #self.size[0] * (self.knobimg_size), self.size[1] * (self.knobimg_size)
	    #do_scale: True
	   # color:
	#	rgba: 1,0,0,.5

        Color:
            rgba: self.knobimg_color
        PushMatrix
        Rotate:
            angle: 360 - self._angle
            origin: self.center
        Rectangle:
            pos: self.pos[0]+ (self.size[0] * (1 - self.knobimg_size)) /2, self.pos[1] + (self.size[1] * (1 - self.knobimg_size)) / 2
            size: self.size[0] * (self.knobimg_size), self.size[1] * (self.knobimg_size) # self.size[0] * (self.knobimg_size), self.size[1] * (self.knobimg_size)
            source: Image(self.file_knob)
	   # do_scale: True

    canvas:
        PopMatrix

''')
class DummyClass: 
	pass

class Toggle_knob(Widget):
    """Class for creating a Knob widget."""

    min = NumericProperty(0)
    '''Minimum value for value :attr:`value`.
    :attr:`min` is a :class:`~kivy.properties.NumericProperty` and defaults
    to 0.
    '''

    max = NumericProperty(100)
    '''Maximum value for value :attr:`value`.
    :attr:`max` is a :class:`~kivy.properties.NumericProperty` and defaults
    to 100.
    '''

    value = NumericProperty(0)
    '''Current value of the knob. Set :attr:`value` when creating a knob to
    set its initial position. An internal :attr:`_angle` is calculated to set
    the position of the knob.
    :attr:`value` is a :class:`~kivy.properties.NumericProperty` and defaults
    to 0.
    '''

    step = BoundedNumericProperty(1, min=0)
    '''Step interval of knob to go from min to max. An internal
    :attr:`_angle_step` is calculated to set knob step in degrees.
    :attr:`step` is a :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to 1 (min=0).
    '''

    curve = BoundedNumericProperty(1, min=1)
    '''This parameter determines the shape of the map function. It represent the
    reciprocal of a power function's exponent used to map the input value.
    So, for higher values of curve the contol is more reactive, and conversely.
    '''

    knobimg_color = ListProperty([1, 1, 1, 1])
    '''Color to apply to :attr:`file_knob` texture when loaded.
    :attr:`knobimg_color` is a :class:`~kivy.properties.ListProperty`
    and defaults to [1,1,1,1].
    '''

    knobimg_size = BoundedNumericProperty(0.9, max=1.0, min=0.1)
    ''' Internal proportional size of rectangle that holds
    :attr:`file_knob` texture.
    :attr:`knobimg_size` is a :class:`~kivy.properties.BoundedNumericProperty`
    and defaults to 0.9.
    '''

    knobimg_bgcolor = ListProperty([0, 0, 0, 1])
    ''' Background color behind :attr:`file_knob` texture.
    :attr:`value` is a :class:`~kivy.properties.ListProperty` and defaults
    to [0,0,0,1].
    '''

 



    _angle          = NumericProperty(0)            # Internal angle calculated from value.
    _angle_step     = NumericProperty(0)            # Internal angle_step calculated from step.
    dummy = DummyClass
    mypath = os.path.dirname(os.path.abspath(inspect.getsourcefile(dummy)))
    file_knob = StringProperty(mypath + os.sep + "toggle_knob.png")
    def __init__(self, *args, **kwargs):
        super(Toggle_knob, self).__init__(*args, **kwargs)
        self.bind(value         =   self._value)
	self.bind(pos           =   self.update_pos)

    def _value(self, instance, value):
        self._angle     =   pow( (value - self.min)/(self.max - self.min), 1./self.curve) * 360.
        self.on_knob(value)

  

    def update_pos(self, *args):
	self.pos =(self.pos[0]+100, self.pos[1])
 
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.update_angle(touch)


    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            self.update_angle(touch)

    def on_touch_up(self,touch):
	if self.collide_point(*touch.pos):
            self.update_angle_f(touch)
########################################################################################################################################
    def update_angle_f(self, touch):
        posx, posy          =   touch.pos
        cx, cy              =   self.center
        rx, ry              =   posx - cx, posy - cy

        if ry >= 0:                                 # Quadrants are clockwise.
            quadrant = 1 if rx >= 0 else 4
        else:
            quadrant = 3 if rx <= 0 else 2

        try:
            angle    = math.atan(rx / ry) * (180./math.pi)
            if quadrant == 2 or quadrant == 3:
                angle = 180 + angle
            elif quadrant == 4:
                angle = 360 + angle

        except:                                   # atan not def for angle 90 and 270
            angle = 90 if quadrant <= 2 else 270

        self._angle_step    =   (self.step*360)/(self.max - self.min)
        self._angle         =   self._angle_step
        while self._angle < angle:
            self._angle     =   self._angle + self._angle_step

        relativeValue   =   pow((angle/360.), 1./self.curve)
        self.value      =   (relativeValue * (self.max - self.min)) + self.min
####################################################################################################################################
    def update_angle(self, touch):
        posx, posy          =   touch.pos
        cx, cy              =   self.center
        rx, ry              =   posx - cx, posy - cy

        if ry >= 0:                                 # Quadrants are clockwise.
            quadrant = 1 if rx >= 0 else 4
        else:
            quadrant = 3 if rx <= 0 else 2

        try:
            angle    = math.atan(rx / ry) * (180./math.pi)
            if quadrant == 2 or quadrant == 3:
                angle = 180 + angle
            elif quadrant == 4:
                angle = 360 + angle

        except:                                   # atan not def for angle 90 and 270
            angle = 90 if quadrant <= 2 else 270

        self._angle_step    =   (self.step*360)/(self.max - self.min)
        self._angle         =   self._angle_step
        while self._angle < angle:
            self._angle     =   self._angle + self._angle_step

        relativeValue   =   pow((angle/360.), 1./self.curve)
        self.value      =   (relativeValue * (self.max - self.min)) + self.min


    #TO OVERRIDE
    def on_knob(self, value):
        pass #Knob values listenerr
