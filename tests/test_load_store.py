import pytest

from arm_leg.components.central_processing_unit import CPU
from arm_leg.instructions.d_format import LoadWord, StoreWord


class LoadStoreTests:
    def test_stores(self) -> None:
        cpu = CPU()
        cpu.registers[0] = StoreWord(rn=1, rt=2, dt_address=0)
        cpu.registers[2] = 42
        cpu.execute_instruction()

        assert cpu.memory[1] == 42

    def test_loads(self) -> None:
        cpu = CPU()
        cpu.registers[0] = LoadWord(rn=1, rt=2, dt_address=0)
        cpu.memory[1] = 24
        cpu.execute_instruction()

        assert cpu.registers[1] == 24

    def test_load_overwrite(self) -> None:
        cpu = CPU()
        cpu.registers[0] = LoadWord(rn=1, rt=2, dt_address=0)
        cpu.registers[2] = 42
        cpu.memory[1] = 24
        cpu.execute_instruction()

        assert cpu.registers[1] == 42

    def test_load_overwrite(self) -> None:
        cpu = CPU()
        cpu.register[0] = StoreWord(rn=1, rt=2, dt_address=0)
        cpu.registers[2] = 24
        cpu.memory[1] = 42
        cpu.execute_instruction()

        assert cpu.memory[1] == 24
