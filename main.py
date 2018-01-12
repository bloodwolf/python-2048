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
        data['status'] = b.status
        e.refreshScreen(data)
        while True:
            action = e.getInput()
            if b.status == 'playing':
                if action == e.KEY_LEFT:
                    b.move('left')
                elif action == e.KEY_RIGHT:
                    b.move('right')
                elif action == e.KEY_UP:
                    b.move('up')
                elif action == e.KEY_DOWN:
                    b.move('down')
                elif action == ord('q'):
                    b.status = 'over'
            elif b.status == 'over':
                if action == ord('q'):
                    break
            if action == ord('r'):
                b.restart()

            data['score'] = b.score
            data['grids'] = b.grids
            data['status'] = b.status
            e.refreshScreen(data)
            if b.isOver():
                b.status = 'over'
    finally:
        e.end()

if __name__ == '__main__':
    main()
