class Tile:
	
	def __init__(self,sym, x,y):
		self.sym = sym
		self.x = x
		self.y = y
		self.alive = False
	def logic(self): #checks if alive
		
		if self.alive == True:
			self.sym = ' '
		if self.alive == False:
			self.sym = ' '
	def addCells(self,map):
			
		neighbourAlives = 0
		for yn in range(-1,2):
			for xn in range(-1,2):
				if self.x > 1 and self.x < 97 and self.y > 1 and self.y < 97:

					if map[self.y+yn][self.x+xn].alive == True:

						if not (yn == 0 and xn == 0):
							neighbourAlives+=1
		if neighbourAlives ==3:
			self.alive = True
		

	def removeCells(self, map):
			
		neighbourAlives = 0
		for yn in range(-1,2):
			for xn in range(-1,2):
				if self.x > 1 and self.x < 97 and self.y > 1 and self.y < 97:
					if map[self.y+yn][self.x+xn].alive == True:
						if not (yn == 0 and xn == 0):
							neighbourAlives+=1
		if neighbourAlives < 2:
			self.alive = False
		if neighbourAlives > 3:
			self.alive = False
