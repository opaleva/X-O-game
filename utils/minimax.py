from __future__ import annotations
from utils.x_o_grid import Sign, Grid, Move


def minimax(grid: Grid, maximizing: bool, current_player: Sign, max_depth: int = 8) -> float:
    if grid.win or grid.standoff or max_depth == 0:
        return grid.assess(current_player)

    if maximizing:
        best_case: float = float('-inf')
        for move in grid.possible_moves:
            result: float = minimax(grid.move(move), False, current_player, max_depth - 1)
            best_case = max(result, best_case)
        return best_case
    else:
        worst_case: float = float('inf')
        for move in grid.possible_moves:
            result = minimax(grid.move(move), True, current_player, max_depth - 1)
            worst_case = min(result, worst_case)
        return worst_case


def search_best_move(grid: Grid, max_depth: int = 8) -> Move:
    best_case: float = float('-inf')
    best_move: Move = Move(-1)
    for move in grid.possible_moves:
        result: float = minimax(grid.move(move), False, grid.turn, max_depth)
        if result > best_case:
            best_case = result
            best_move = move
    return best_move
