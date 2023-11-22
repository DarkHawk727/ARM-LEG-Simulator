from abc import ABC, abstractmethod

from arm_leg.components.data_memory import DataMemory
from arm_leg.components.register_file import RegisterFile
from arm_leg.instructions.opcodes import Opcode


class DFormatInstruction(ABC):
    _opcode: Opcode
    _rn: int
    _rt: int
    _dt_address: int

    def __init__(self, rn: int, rt: int, dt_address: int) -> None:
        self._rn = rn
        self._rt = rt
        self._dt_address = dt_address

    def __str__(self) -> str:
        return f"{self._opcode.name} X{self._rn} [X{self._rd}, #{self._constant}]"

    @abstractmethod
    def execute(self, registers: RegisterFile, memory: DataMemory) -> None:
        pass


class LoadWord(DFormatInstruction):
    _opcode = Opcode.LDUR

    def execute(self, registers: RegisterFile, memory: DataMemory) -> None:
        registers[self._rt] = memory[self._rn + self._dt_address]


class StoreWord(DFormatInstruction):
    _opcode = Opcode.STUR

    def execute(self, registers: RegisterFile, memory: DataMemory) -> None:
        memory[self._rn + self._dt_address] = registers[self._rt]
