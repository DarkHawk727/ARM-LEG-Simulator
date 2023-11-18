from abc import ABC, abstractmethod

from components.register_file import RegisterFile
from opcodes import Opcode


class IFormatInstruction(ABC):
    _opcode: Opcode
    _rn: int
    _rd: int
    _constant: int

    def __init__(self, rn: int, rd: int, constant: int) -> None:
        self._rn = rn
        self._rd = rd
        self._constant = constant

    def __str__(self) -> str:
        return f"{self._opcode.name} X{self._rn}, X{self._rd}, #{self._constant}"

    @abstractmethod
    def execute(self, registers: RegisterFile) -> None:
        pass


class AddImmediate(IFormatInstruction):
    _opcode = Opcode.ADDI

    def execute(self, registers: RegisterFile) -> None:
        registers[self._rd] = registers[self._rn] + self._constant


class SubImmediate(IFormatInstruction):
    _opcode = Opcode.SUBI

    def execute(self, registers: RegisterFile) -> None:
        registers[self._rd] = registers[self._rn] - self._constant
