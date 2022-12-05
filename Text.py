import Component

class Text(Component):
	#Class Variables:
	#Component:
	#	posX
	#	posY
	#	color
	#value

	#__init__() inherited from Component
	#__init__() defined from this class is not needed due to inheritance
	#This is needed only if new variables are introduced into the constructor
		#def __init__(self, newPosX, newPosY):
		#	Component.__init__(self, newPosX, newPosY)

	def getText(self):
		return self.value

	def setText(self, newValue):
		self.value = newValue