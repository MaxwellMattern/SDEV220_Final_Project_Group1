import Component

class Symbol(Component):
	#Class Variables:
	#Component:
	#	posX
	#	posY
	#	color
	#typeID
	#scaleFactor

	def __init__(self, newPosX, newPosY, newTypeID):
		Component.__init__(self, newPosX, newPosY)
		self.typeID = newTypeID

	def getType(self):
		return self.typeID
	def getScale(self):
		return self.scaleFactor

	def setType(self, newTypeID):
		self.typeID = newTypeID
	def setScale(self, newScaleFactor):
		self.scaleFactor = newScaleFactor