from abc import ABC, abstractmethod

from components.register_file import RegisterFile
from components.data_memory import DataMemory

from opcodes import Opcode


class CBFormatInstruction(ABC):
    _opcode: Opcode
    _rt: int
    _br_address: int

    def __init__(self, rt: int, br_address: int) -> None:
        self._rt = rt
        self._dt_address = br_address

    def __str__(self) -> str:
        return f"{self._opcode.name} X{self._rn} [X{self._rd}, #{self._constant}]"

    @abstractmethod
    def execute(self, registers: RegisterFile, program_counter: int) -> None:
        pass


class BranchOnZero(CBFormatInstruction):
    _opcode = Opcode.CBZ

    def execute(self, registers: RegisterFile, program_counter: int) -> None:
        if registers[self._rt] == 0:
            program_counter += 4 * self._br_address
        else:
            program_counter += 4  # Is this necessary?


class BranchOnNonZero(CBFormatInstruction):
    _opcode = Opcode.CBNZ

    def execute(self, registers: RegisterFile, program_counter: int) -> None:
        if registers[self._rt] != 0:
            program_counter += 4 * self._br_address
        else:
            program_counter += 4  # Is this necessary?
