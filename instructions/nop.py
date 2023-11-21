from opcodes import Opcode

class NoOperation:
    def __init__(self) -> None:
        self._opcode: Opcode = Opcode.NOP
    
    def __str__(self):
        return f"{self._opcode.name}"
