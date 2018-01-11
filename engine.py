import curses

class Engine(object):
    def __init__(self):
        self.screen = curses.initscr()
        self.screen.keypad(1)
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.curs_set(0)

        self.KEY_UP = curses.KEY_UP
        self.KEY_DOWN = curses.KEY_DOWN
        self.KEY_LEFT = curses.KEY_LEFT
        self.KEY_RIGHT = curses.KEY_RIGHT

    def initScreen(self):
        self.screen.border()
        ret = []
        ret.append('              score:    0')
        ret.append('-------------------------')
        ret.append('|     |     |     |     |')
        ret.append('-------------------------')
        ret.append('|     |     |     |     |')
        ret.append('-------------------------')
        ret.append('|     |     |     |     |')
        ret.append('-------------------------')
        ret.append('|     |     |     |     |')
        ret.append('-------------------------')

        for i, line in enumerate(ret):
            self.screen.addstr(i + 12, 25, line)
        self.screen.refresh()

    def refreshScreen(self, data):
        self.screen.addstr(12, 45, '% 5d' % data['score'])
        for i in range(4):
            for j in range(4):
                if data['grids'][i][j] != 0:
                    value = '%5s' % (data['grids'][i][j])
                else:
                    value = '     '
                self.screen.addstr(14 + i * 2, 26 + j * 6, value, curses.color_pair(data['color'][data['grids'][i][j]]))
        self.screen.addstr(12, 49, '')
        self.screen.refresh()

    def getInput(self):
        return self.screen.getch()

    def end(self):
        self.screen.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
