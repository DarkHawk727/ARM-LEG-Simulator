from __future__ import annotations

from typing import List, Union
from arm_leg.instructions.instruction import Instruction

MemoryValue = Union[int, Instruction]


class RegisterFile:
    def __init__(self) -> None:
        self._storage: List[MemoryValue] = [0] * 32

    def __getitem__(self, position: int) -> MemoryValue:
        return self._storage[position]

    def __setitem__(self, position: int, value: MemoryValue) -> None:
        if position < 31:
            self._storage[position] = value
        else:
            raise IndexError("Cannot modify XZR!")
