#!/usr/bin/env python

import random
import curses

class Board(object):
    newvalues = (2, 4)

    def __init__(self):
        self.grids = []
        self.score = 0
        self.screen = curses.initscr()
        self.screen.keypad(1)
        curses.noecho()
        curses.cbreak()
        for row in range(4):
            tmp = []
            for column in range(4):
                tmp.append(0)
            self.grids.append(tmp)

        for t in range(2):
            (i, j) = self.getRandomGrid()
            self.grids[i][j] = random.choice(Board.newvalues)

    def left(self):
        newgrids = []
        for row in self.grids:
            newgrids.append(self.transformRow(row))
        self.grids = newgrids

    def right(self):
        self.rotateClockwise(180)
        self.left()
        self.rotateClockwise(180)

    def up(self):
        self.rotateClockwise(270)
        self.left()
        self.rotateClockwise(90)

    def down(self):
        self.rotateClockwise(90)
        self.left()
        self.rotateClockwise(270)

    def move(self, direction):
        oldGrids = []
        for x in self.grids:
            oldGrids.append(x[:])
        getattr(self, direction)()
        if not self.isSame(oldGrids):
            self.generateNewGrid()

    def output(self):
        ret = []
        ret.append('score: %d' % (self.score))
        for i in range(4):
            ret.append('-' * 25)
            tmp = ''
            for j in range(4):
                outputstr = str(self.grids[i][j])
                if outputstr == '0':
                    outputstr = ''
                tmp += '|%5s' % (outputstr)
            tmp += '|'
            ret.append(tmp)
        ret.append('-' * 25)
        return ret

    def cursesOutput(self):
        self.screen.border(0)
        for i, line in enumerate(self.output()):
            self.screen.addstr(12 + i, 25, line)
        self.screen.refresh()

    def getRandomGrid(self):
        while True:
            r = random.randint(0, 15)
            i = int(r / 4)
            j = r % 4
            if self.grids[i][j] == 0:
                return (i, j)

    def transformRow(self, row):
        row = [x for x in row if x != 0]
        index = 0
        while index <= len(row) - 2:
            if row[index] == row[index + 1]:
                row[index] *= 2
                row[index + 1] = 0
                self.score += row[index]
                index += 2
            else:
                index += 1
        row = [x for x in row if x != 0]
        for i in range(4 - len(row)):
            row.append(0)
        return row

    def generateNewGrid(self):
        (i, j) = self.getRandomGrid()
        self.grids[i][j] = Board.newvalues[random.randint(0, len(Board.newvalues) - 1)]

    def isOver(self):
        for i in range(4):
            for j in range(4):
                if self.grids[i][j] == 0:
                    return False
        for i in range(4):
            for j in range(3):
                if self.grids[i][j] == self.grids[i][j + 1]:
                    return False
        for i in range(4):
            for j in range(3):
                if self.grids[j][i] == self.grids[j + 1][i]:
                    return False
        return True

    def isSame(self, oldGrids):
        for i in range(4):
            for j in range(4):
                if self.grids[i][j] != oldGrids[i][j]:
                    return False
        return True

    def rotateClockwise(self, degree):
        oldGrids = []
        for x in self.grids:
            oldGrids.append(x[:])
        if degree == 90:
            for i in range(4):
                for j in range(4):
                    self.grids[i][j] = oldGrids[3 - j][i]
        elif degree == 180:
            for i in range(4):
                for j in range(4):
                    self.grids[i][j] = oldGrids[3 - i][3 - j]
        elif degree == 270:
            for i in range(4):
                for j in range(4):
                    self.grids[i][j] = oldGrids[j][3 - i]

    def getInput(self):
        return self.screen.getch()

    def run(self):
        pass

def main():
    b = Board()
    b.cursesOutput()
    while True:
        action = b.getInput()
        if action == curses.KEY_LEFT:
            b.move('left')
        elif action == curses.KEY_RIGHT:
            b.move('right')
        elif action == curses.KEY_UP:
            b.move('up')
        elif action == curses.KEY_DOWN:
            b.move('down')

        b.cursesOutput()
        if b.isOver():
            break
    curses.endwin()
    print(b.score)

if __name__ == '__main__':
    main()
