import curses
import copy
from world.tile import Tile
def init():
	
	
	stdscr = curses.initscr()
	stdscr.clear()
	stdscr.refresh()
	stdscr.getkey()
		
	curses.noecho()
	curses.cbreak()
	curses.halfdelay(10)
	stdscr.keypad(True)
	begin_x = 20
	begin_y = 7
	height = 5
	width = 40
	win = curses.newwin(height,width,begin_y,begin_x)
	pad = curses.newpad(100,100)
	return stdscr, win, pad
	
def loop(stdscr, win, pad):

	isSetting = False
	running = True
	mapWidth = 99
	mapHeight = 99
	cursorX = 0
	cursorY = 0
	map = [[0 for x in range(mapWidth)] for y in range(mapHeight)]
	for y in range(mapWidth):
		for x in range(mapHeight):
			map[y][x] = Tile('0', x,y)
	while(running == True):





		stdscr.addstr(0,0, 'Game Of Life', curses.A_REVERSE)
		mode = 'RUN'
		if isSetting == False:
			mode = 'SET'
		stdscr.addstr(1,0, 'MODE: ' + mode, curses.A_REVERSE)
		stdscr.refresh()




		for y in range (0,mapWidth):
			for x in range (0,mapHeight):
				map[y][x].logic()		
				if x == cursorX and y == cursorY:
					pad.addch(y,x,ord(str(map[y][x].sym)), curses.A_UNDERLINE)
				elif map[y][x].alive == True:
					pad.addch(y,x,ord(str(map[y][x].sym)), curses.A_REVERSE)
				else:
					pad.addch(y,x,ord(str(map[y][x].sym)))


		pad.refresh(0,0,5,5,20,75)

		if isSetting == True:	
			changeMap = copy.deepcopy(map)
			for y in range (0,mapWidth):
				for x in range (0,mapHeight):
					map[y][x].addCells(changeMap)			

			for y in range (0,mapWidth):
				for x in range (0,mapHeight):
					map[y][x].removeCells(changeMap)
		
		c = stdscr.getch()
		if c == ord('g'):
			isSetting = not isSetting
		elif c == ord('w'):
			cursorY -=1
		elif c == ord('a'):
			cursorX -=1
		elif c == ord('s'):
			cursorY +=1
		elif c == ord('d'):	
			cursorX +=1
		elif c == ord('x'):
			map[cursorY][cursorX].alive = True

		
			
				
		elif c == ord('q'):
			running = False
			
	quit(stdscr)	



def run():
	stdscr, win, pad = init()
	loop(stdscr, win,pad)
def quit(stdscr):
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()

run()

