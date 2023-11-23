from __future__ import annotations

from typing import Protocol

from arm_leg.instructions.opcodes import Opcode


class Instruction(Protocol):
    _opcode: Opcode

    def __init__(self, **kwargs) -> None:
        ...

    def __str__(self) -> str:
        ...

    def __eq__(self, other: Instruction) -> bool:
        ...

    def execute(self, **kwargs) -> None:
        ...
