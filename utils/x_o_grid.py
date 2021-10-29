from __future__ import annotations
from typing import NewType
from abc import ABC, abstractmethod

Move = NewType('Move', int)


class Sign:
    @property
    def is_next(self) -> Sign:
        raise NotImplementedError('Должен вызываться подклассами.')


class Grid(ABC):
    @property
    @abstractmethod
    def turn(self) -> Sign:
        ...

    @abstractmethod
    def move(self, location: Move) -> Grid:
        ...

    @property
    @abstractmethod
    def possible_moves(self) -> list[Move]:
        ...

    @property
    @abstractmethod
    def win(self) -> bool:
        ...

    @property
    def standoff(self) -> bool:
        return (not self.win) and (len(self.possible_moves) == 0)

    @abstractmethod
    def assess(self, player: Sign) -> float:
        ...
