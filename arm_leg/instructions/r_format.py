from abc import ABC, abstractmethod

from arm_leg.components.register_file import RegisterFile
from arm_leg.instructions.instruction import Instruction
from arm_leg.instructions.opcodes import Opcode


class RFormatInstruction(ABC):
    _opcode: Opcode
    _rm: int
    _rn: int
    _rd: int

    def __init__(self, rn: int, rd: int, rm: int) -> None:
        self._rm = rm
        self._rn = rn
        self._rd = rd

    def __str__(self) -> str:
        return f"{self._opcode.name} X{self._rn}, X{self._rd}, X{self._rm}"

    def __eq__(self, other: Instruction) -> bool:
        if not (self._opcode == other._opcode):
            return False
        return (self._rn == other._rn and
                self._rd == other._rd and
                self._rm == other._rm)

    @abstractmethod
    def execute(self, registers: RegisterFile) -> None:
        pass


class Add(RFormatInstruction):
    _opcode = Opcode.ADD

    def execute(self, registers: RegisterFile) -> None:
        registers[self._rd] = registers[self._rn] + registers[self._rm]


class Sub(RFormatInstruction):
    _opcode = Opcode.SUB

    def execute(self, registers: RegisterFile) -> None:
        registers[self._rd] = registers[self._rn] - registers[self._rm]


class LeftShift(RFormatInstruction):
    _opcode = Opcode.LSL

    def execute(self, registers: RegisterFile) -> None:
        registers[self._rd] = registers[self._rn] << registers[self._rm]


class RightShift(RFormatInstruction):
    _opcode = Opcode.RSL

    def execute(self, registers: RegisterFile) -> None:
        registers[self._rd] = registers[self._rn] >> registers[self._rm]


class And(RFormatInstruction):
    _opcode = Opcode.AND

    def execute(self, registers: RegisterFile) -> None:
        registers[self._rd] = registers[self._rn] & registers[self._rm]


class Orr(RFormatInstruction):
    _opcode = Opcode.ORR

    def execute(self, registers: RegisterFile) -> None:
        registers[self._rd] = registers[self._rn] | registers[self._rm]


class Eor(RFormatInstruction):
    _opcode = Opcode.EOR

    def execute(self, registers: RegisterFile) -> None:
        registers[self._rd] = registers[self._rn] ^ registers[self._rm]
