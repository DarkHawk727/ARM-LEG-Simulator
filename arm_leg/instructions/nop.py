from arm_leg.instructions.instruction import Instruction
from arm_leg.instructions.opcodes import Opcode


class NoOperation:
    def __init__(self) -> None:
        self._opcode: Opcode = Opcode.NOP

    def __str__(self):
        return f"{self._opcode.name}"

    def __eq__(self, other: Instruction) -> bool:
        return self._opcode == other._opcode
