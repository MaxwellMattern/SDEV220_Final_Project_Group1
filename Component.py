

class Component:
	#Class Variables:
	#posX
	#posY
	#color
	
	def __init__(self, newPosX, newPosY):
		self.posX = newPosX
		self.posY = newPosY


	def getX(self):
		return self.posX
	def getY(self):
		return self.posY
	def getColor(self):
		return self.color


	def setX(self, newPosX):
		self.posX = newPosX
	def setY(self, newPosY):
		self.posY = newPosY
	def setColor(self, newColor):
		self.color = newColor
