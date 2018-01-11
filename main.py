import game
import engine

def main():
    try:
        b = game.Board()
        e = engine.Engine()
        e.initScreen()
        data = {}
        data['score'] = b.score
        data['grids'] = b.grids
        data['color'] = b.color
        e.refreshScreen(data)
        while True:
            action = e.getInput()
            if action == e.KEY_LEFT:
                b.move('left')
            elif action == e.KEY_RIGHT:
                b.move('right')
            elif action == e.KEY_UP:
                b.move('up')
            elif action == e.KEY_DOWN:
                b.move('down')

            data['score'] = b.score
            data['grids'] = b.grids
            e.refreshScreen(data)
            if b.isOver():
                break
    finally:
        e.end()
        print b.score

if __name__ == '__main__':
    main()
