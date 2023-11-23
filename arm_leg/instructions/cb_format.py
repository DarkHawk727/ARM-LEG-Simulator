from abc import ABC, abstractmethod

from arm_leg.components.register_file import RegisterFile
from arm_leg.instructions.instruction import Instruction
from arm_leg.instructions.opcodes import Opcode


class CBFormatInstruction(ABC):
    _opcode: Opcode
    _rt: int
    _br_address: int

    def __init__(self, rt: int, br_address: int) -> None:
        self._rt = rt
        self._br_address = br_address

    def __str__(self) -> str:
        return f"{self._opcode.name} X{self._rn} [X{self._rd}, #{self._constant}]"

    def __eq__(self, other: Instruction) -> bool:
        if not (self._opcode == other._opcode):
            return False
        return self._rt == other._rt and self._br_address == other._br_address

    @abstractmethod
    def execute(self, registers: RegisterFile, program_counter: int) -> None:
        pass


class BranchOnZero(CBFormatInstruction):
    _opcode = Opcode.CBZ

    def execute(self, registers: RegisterFile, program_counter: int) -> int:
        if registers[self._rt] == 0:
            return program_counter + 4 * self._br_address
        else:
            return program_counter + 4  # Is this necessary?


class BranchOnNonZero(CBFormatInstruction):
    _opcode = Opcode.CBNZ

    def execute(self, registers: RegisterFile, program_counter: int) -> int:
        if registers[self._rt] != 0:
            return program_counter + 4 * self._br_address
        else:
            return program_counter + 4  # Is this necessary?
