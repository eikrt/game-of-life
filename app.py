import curses
def init():
	
	
	stdscr = curses.initscr()
	stdscr.clear()
	stdscr.refresh()
	stdscr.getkey()
	
	curses.noecho()
	curses.cbreak()
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
	map = [[0 for x in range(99)] for y in range(99)]
	
	while(running == True):




		stdscr.addstr(0,0, 'Game Of Life', curses.A_REVERSE)
		stdscr.refresh()

		for y in range (0,mapWidth):
			for x in range (0,mapHeight):
				pad.addch(y,x,ord(str(map[x][y])))
		pad.refresh(0,0,5,5,20,75)
		
		c = stdscr.getch()
		if c == ord('q'):
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

