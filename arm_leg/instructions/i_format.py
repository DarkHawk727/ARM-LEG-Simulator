from abc import ABC, abstractmethod

from arm_leg.components.register_file import RegisterFile
from arm_leg.instructions.instruction import Instruction
from arm_leg.instructions.opcodes import Opcode


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

    def __eq__(self, other: Instruction) -> bool:
        if not (self._opcode == other._opcode):
            return False
        return (
            self._rn == other._rn
            and self._rd == other._rd
            and self._constant == other._constant
        )

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
