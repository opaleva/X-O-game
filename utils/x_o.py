from __future__ import annotations
from enum import Enum
from utils.x_o_grid import Sign, Grid, Move


class GameSign(Sign, Enum):
    X = '×'
    O = '○'
    N = ' '

    @property
    def is_next(self) -> GameSign:
        if self == GameSign.X:
            return GameSign.O
        elif self == GameSign.O:
            return GameSign.X
        else:
            return GameSign.N

    def __str__(self) -> str:
        return self.value


class GameGrid(Grid):
    # В действительности position неизменяемый; задаётся именно в аргументах для x_o_ai.py
    def __init__(self, position: list[GameSign] = [GameSign.N] * 9, turn: GameSign = GameSign.X) -> None:
        self.position: list[GameSign] = position
        self._turn: GameSign = turn

    @property
    def turn(self) -> Sign:
        return self._turn

    def move(self, location: Move) -> Grid:
        current_position: list[GameSign] = self.position.copy()
        current_position[location] = self._turn
        return GameGrid(current_position, self._turn.is_next)

    @property
    def possible_moves(self) -> list[Move]:
        return [Move(i) for i in range(len(self.position)) if self.position[i] == GameSign.N]

    @property
    def win(self) -> bool:
        return (self.position[0] == self.position[1] and self.position[0] == self.position[2] and self.position[0] != GameSign.N or
                self.position[3] == self.position[4] and self.position[3] == self.position[5] and self.position[3] != GameSign.N or
                self.position[6] == self.position[7] and self.position[6] == self.position[8] and self.position[6] != GameSign.N or
                self.position[0] == self.position[3] and self.position[0] == self.position[6] and self.position[0] != GameSign.N or
                self.position[1] == self.position[4] and self.position[1] == self.position[7] and self.position[1] != GameSign.N or
                self.position[2] == self.position[5] and self.position[2] == self.position[8] and self.position[2] != GameSign.N or
                self.position[0] == self.position[4] and self.position[0] == self.position[8] and self.position[0] != GameSign.N or
                self.position[2] == self.position[4] and self.position[2] == self.position[6] and self.position[2] != GameSign.N)

    def assess(self, player: Sign) -> float:
        if self.win and self.turn == player:
            return -1
        elif self.win and self.turn != player:
            return 1
        else:
            return 0

    def __repr__(self) -> str:
        return f' {self.position[0]} | {self.position[1]} | {self.position[2]} \n' \
               f'{"—" * 11}\n' \
               f' {self.position[3]} | {self.position[4]} | {self.position[5]} \n' \
               f'{"—" * 11}\n' \
               f' {self.position[6]} | {self.position[7]} | {self.position[8]}'
