import curses
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

	running = True
	mapWidth = 99
	mapHeight = 99
	cursorX = 0
	cursorY = 0
	map = [[0 for x in range(99)] for y in range(99)]
	for y in range(99):
		for x in range(99):
			map[y][x] = Tile('0', x,y)
	while(running == True):




		stdscr.addstr(0,0, 'Game Of Life', curses.A_REVERSE)
		stdscr.refresh()

		for y in range (0,mapWidth):
			for x in range (0,mapHeight):
				
				map[x][y].logic(map)
				if x == cursorX and y == cursorY:
					pad.addch(y,x,ord(str(map[x][y].sym)), curses.A_REVERSE)
				else:
					pad.addch(y,x,ord(str(map[x][y].sym)))
				

					


		pad.refresh(0,0,5,5,20,75)
		
		c = stdscr.getch()
		if c == ord('q'):
			running = False
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

			map[cursorY+1][cursorX+1].alive = True

				
			
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

