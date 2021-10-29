from utils.minimax import search_best_move
from utils.x_o import GameGrid
from utils.x_o_grid import Move, Grid

grid: Grid = GameGrid()


def get_move() -> Move:
    next_move: Move = Move(-1)
    while next_move not in grid.possible_moves:
        next_turn: int = int(input('Номер клетки для хода (от 1 до 9): '))
        next_move = Move(next_turn - 1)
    return next_move


if __name__ == '__main__':
    print(' 1 | 2 | 3 \n'
          f'{"—" * 11}\n'
          ' 4 | 5 | 6 \n'
          f'{"—" * 11}\n'
          ' 7 | 8 | 9')
    while True:
        your_move: Move = get_move()
        grid = grid.move(your_move)
        if grid.win:
            print(':)')
            break
        elif grid.standoff:
            print(':|')
            break
        ai_move: Move = search_best_move(grid)
        print(f'Ответный ход – на клетку {ai_move + 1}.')
        grid = grid.move(ai_move)
        print(grid)
        if grid.win:
            print(':(')
            break
        elif grid.standoff:
            print(':|')
            break
