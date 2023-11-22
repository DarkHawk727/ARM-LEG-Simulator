from enum import Enum, auto


class Opcode(Enum):
    ADD = auto()
    SUB = auto()
    ADDI = auto()
    SUBI = auto()
    LDUR = auto()
    STUR = auto()
    B = auto()
    CBZ = auto()
    CBNZ = auto()
    LSL = auto()
    RSL = auto()
    AND = auto()
    ORR = auto()
    XOR = auto()
    NOP = auto()
