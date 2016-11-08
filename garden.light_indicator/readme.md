A simple light indicator. Can use 1,2 or 3 lights.


	Light_indicator class
	A basic Kivy example:

		Light_indicator:
			id:R
			num:3
			color1: 'red'
			bol1: True
			color2:'yellow'
			color3:'green'
			setting_on: False
			pos_l1: [25,100]
			pos_l2: [100,100]
			pos_l3: [175,100]
			label_on: True
			text_size: 15
			l1_label: "Off"
			l2_label: "Warming"
			l3_label: "On"

		Light_indicator:
			orientation: 'vertical'# orientation of the light. defaults to 'horizontal'.
			size_lights: [50,50] # size of light. (x-axis, y-axis) of an ellipse. defauts to [50,50]
			num:3
			color1: 'red'
			bol1: True
			color2:'yellow'
			color3:'green'
			setting: True
			pos_l1: [100,175]
			pos_l2: [100,100]
			pos_l3: [100,25]
			label_on: True
			text_size: 15
			l1_label: "Off"
			l2_label: "Warming"
			l3_label: "On"
Note: The positions of the labels are determined by the positions of the lights.
