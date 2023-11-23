from abc import ABC, abstractmethod

from arm_leg.instructions.instruction import Instruction
from arm_leg.instructions.opcodes import Opcode


class BFormatInstruction(ABC):
    _opcode: Opcode
    _br_address: int

    def __init__(self, br_address: int) -> None:
        self._br_address = br_address

    def __str__(self) -> str:
        return f"{self._opcode.name} #{self._br_address}"

    def __eq__(self, other: Instruction) -> bool:
        if not (self._opcode == other._opcode):
            return False
        return self._br_address == other._br_address

    @abstractmethod
    def execute(self, program_counter: int) -> None:
        pass


class UnconditionalBranch(BFormatInstruction):
    _opcode = Opcode.B

    def execute(self, program_counter: int) -> None:
        program_counter += 4 * self._br_address
