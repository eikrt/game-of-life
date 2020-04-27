class Tile:
	
	def __init__(self,sym, x,y):
		self.sym = sym
		self.x = x
		self.y = y
		self.alive = False
	def logic(self, map):
		neighbourAlives = 0
		for xn in range(3):
			for yn in range(3):
				if self.x > 1 and self.x < 98 and self. y > 1 and self.y < 98:
					if map[self.x-1+xn][self.y-1+yn].alive == True:
						neighbourAlives+=1
		if neighbourAlives < 2:
			self.alive = False
		if neighbourAlives == 2 or neighbourAlives == 3:
			self.alive = True
		if neighbourAlives > 3:
			self.alive = False
		if self.alive == True:
			self.sym = 1
		if self.alive == False:
			self.sym = 0	
				
