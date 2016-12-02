A simple light indicator. Can use 1,2 or 3 lights.


	Light_indicator class
	A basic Kivy example:

		Light_indicator:
			num:3 # number of lights.
			color1: 'red' #Color of light 1. default to yellow
			bol1: True # Boolean to turn light1 off/on.
			color2:'yellow'#Color of light 2.default to yellow
			color3:'green' #Color of light 3.default to yellow
			setting_on: False # Background setting off default to True
			pos_l1: [25,100] # positions of Light 1 in (x , y). defualt to (100,100)
			pos_l2: [100,100]
			pos_l3: [175,100]

		Light_indicator:
			orientation: 'vertical'# orientation of the light. defaults to 'horizontal'.
			size_lights: [50,50] # size of light. (x-axis, y-axis) of an ellipse. defauts to [50,50]
			num:3
			color1: 'red'
			bol1: True
			color2:'yellow'
			color3:'green'
			setting_on: True
			pos_l1: [100,175]
			pos_l2: [100,100]
			pos_l3: [100,25]

