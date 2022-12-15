import Component

class Line(Component):
	#Class Variables:
	#Component:
	#	posX
	#	posY
	#	color
	#start
	#end
	#turns[]
	#style

	#__init__() inherited from Component
	#__init__() defined from this class is not needed due to inheritance
	#This is needed only if new variables are introduced into the constructor
		#def __init__(self, newPosX, newPosY):
		#	Component.__init__(self, newPosX, newPosY)

	def getStart(self):
		return self.start#Returns a Component object
	def getEnd(self):
		return self.end#Returns a Component object
	def getTurns(self):
		return self.turns#Returns a list
	def getStyle(self):
		return self.style#Returns a String

	def setStart(self, newStart):#Requires a Component object
		self.start = newStart
	def setEnd(self, newEnd):#Requires a Component object
		self.end = newEnd
	def setTurns(self, newTurns):#Requires a list
		self.turns = newTurns
	def setStyle(self, newStyle):#Requires a String
		self.style = newStyle